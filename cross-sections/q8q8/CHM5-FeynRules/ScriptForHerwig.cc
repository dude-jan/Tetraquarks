#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

char* inputFile;
bool inputFlag = 0;
bool foundName = 0;

int main(int argc, char* argv[])
{
    /*Used special characters*/
    vector<string> chars;
    chars.push_back("\\");
    chars.push_back("<");
    chars.push_back(">");
    chars.push_back(":");
    /*Often used variables*/
    fstream input;
    fstream lhcin;
    fstream paramcard;
    vector<string> inputParamNames;
    vector<string> inputParamValues;
    vector<string> lhcinBuf;
    vector<string> paramNames;

    vector<string> protectedParams;

    vector<string> particlesIn;
    vector<string> particlesOut;

    string processes = "none";
    bool rivet = 0;

    bool processedIn = 0;
    bool processedOut = 0;

    /*Check arguments*/
    if (argc == 1)  //No arguments specified
    {
        printf("No arguments specified - zero all parameters\n");
    }
    else if (argc == 2) //Inputfile specified
    {
        inputFile = argv[1];
        printf("Using parameters from ");
        cout << inputFile << endl;
        input.open(inputFile, ios::in);
        if (input.is_open())
        {
            string inputLine;
            string temp = "";
            while (getline(input, inputLine)) //read data from file object and put it into string.
            {
                if (inputLine[0] != '#' && !inputLine.empty())//Filter comments and empty lines
                {
                    //First, try to process special characters
                    if (inputLine[0] == '\\')
                    {
                        inputLine.erase(0, 1);
                        protectedParams.push_back(inputLine);
                    }
                    else if (inputLine[0] == '<')
                    {
                        inputLine.erase(0, 1);
                        particlesIn.push_back(inputLine);
                    }
                    else if (inputLine[0] == '>')
                    {
                        inputLine.erase(0, 1);
                        particlesOut.push_back(inputLine);
                    }
                    else if (inputLine[0] == ':')
                    {
                        inputLine.erase(0, 1);
                        while (inputLine[0] != ' ' && inputLine.length() > 0)
                        {
                            temp += inputLine[0];
                            inputLine.erase(0, 1);
                        }
                        inputLine.erase(0,1);
                        if(temp == "Processes")
                        {
                            processes = inputLine;
                        }
                        else if(temp == "RivetAnalysis")
                        {
                            if(inputLine == "1")
                            {
                                rivet = 1;
                            }
                        }
                        temp = "";
                    }
                    //Masses and couplings
                    else
                    {
                        while (inputLine[0] != ' ' && inputLine.length() > 0)
                        {
                            temp += inputLine[0];
                            inputLine.erase(0, 1);
                        }
                        inputLine.erase(0, 1);  //Delete space bar
                        inputParamNames.push_back(temp);
                        temp = "";
                        while (inputLine.length() > 0)
                        {
                            temp += inputLine[0];
                            inputLine.erase(0, 1);
                        }
                        inputParamValues.push_back(temp);
                        temp = "";
                    }
                }
            }
            input.close();
        }
        else
        {
            printf("Error: Could not find input file..\n");
            return 0;
        }
    }
    else //Something is wrong with parameters
    {
        printf("Error: Illegal number of parameters\n");
        return 0;
    }

    /*Buffer LHC-FRModel.in*/
    lhcin.open("LHC-FRModel.in", ios::in);  // open a file to perform write operation using file object
    if (lhcin.is_open()) //checking whether the file is open
    {
        string lhcinLine;
        while (getline(lhcin, lhcinLine))   //Read .in file into buffer
        {
            lhcinBuf.push_back(lhcinLine);
        }
        lhcin.close();
    }
    else
    {
        printf("Error: Could not find .in file\n");
        return 0;
    }

    /*Iterate over param_card.dat*/
    paramcard.open("param_card.dat", ios::in); //Read param card
    if (paramcard.is_open()) //checking whether the file is open
    {  
        string tp;
        while (getline(paramcard, tp)) //read data from file object and put it into string.
        { 
            if (tp[0] != '#' && !tp.empty())   //Filter comments
            {
                foundName = 0;
                while (tp[0] != '#' && tp.length() >= 1)
                {
                    tp.erase(0, 1);
                    if (tp[0] == '#')
                    {
                        foundName = 1;
                    }
                }
                tp.erase(0, 2);
                if (foundName && tp[0] != 'M')
                {
                    /*At this point, tp contains a possible parameter*/
                    //WRITE INTO A VECTOR
                    //cout << tp << "\n"; //print the data of the string
                    paramNames.push_back(tp);
                }
            }
        }
        paramcard.close(); //close the file object.
    }
    else
    {
        printf("Error: Couldn't find param_card\n");
        return 0;
    }


    /*Write new LHC.in*/
    lhcin.open("LHC.in", ios::out | ios::trunc);  // open .in file for write with truncate option
    if (lhcin.is_open()) //checking whether the file is open
    {
        unsigned int i = 0;
        unsigned int j = 0;
        unsigned int k = 0;
        unsigned int p = 0;
        bool usercontained = 0;
        string tempName = "";
        for (i = 0; i < lhcinBuf.size(); i++)
        {
            //RivetAnalysis
            if (lhcinBuf[i] == "saverun LHC-FRModel EventGenerator" && rivet)    //Rivet
            {
                lhcin << "create ThePEG::RivetAnalysis Rivet RivetAnalysis.so" << endl;
                lhcin << "insert EventGenerator:AnalysisHandlers 0 Rivet" << endl;
                lhcin << "read 13TeV.ana" << endl;

            }
            //Particle Processes
            if (lhcinBuf[i].find("set HPConstructor:Processes") != string::npos && processes != "none")
            {
               lhcinBuf[i] = "set HPConstructor:Processes " + processes;
            }
            //Incoming Particles
            if (lhcinBuf[i].find("insert HPConstructor:Incoming 0") != std::string::npos && particlesIn.size() > 0)
            {
                if (!processedIn)   //Custom input particles
                {
                    for (p = 0; p < particlesIn.size(); p++)
                    {
                        lhcin << "insert HPConstructor:Incoming 0 " << particlesIn[p] << endl;
                    }
                    processedIn = 1;
                }
                if(lhcinBuf[i][0] != '#')
                {
                    tempName = '#' + lhcinBuf[i];
                    lhcinBuf[i] = tempName;
                    tempName = "";
                }
            }
            //Outgoing Particles
            if (lhcinBuf[i].find("insert HPConstructor:Outgoing 0") != std::string::npos && particlesOut.size() > 0)
            {
                if (!processedOut)   //Custom input particles
                {
                    for (p = 0; p < particlesOut.size(); p++)
                    {
                        lhcin << "insert HPConstructor:Outgoing 0 " << particlesOut[p] << endl;
                    }
                    processedOut = 1;
                }
                if(lhcinBuf[i][0] != '#')
                {
                    tempName = '#' + lhcinBuf[i];
                    lhcinBuf[i] = tempName;
                    tempName = "";
                }
            }

            lhcin << lhcinBuf[i] << endl;   //Copy from buffer

            if (lhcinBuf[i] == "cd /Herwig/NewPhysics")    //Modify after this line
            {
                lhcin << endl;
                lhcin << "########################" << endl;
                lhcin << "## Modified Couplings ##" << endl;
                lhcin << "########################" << endl;
                for (j = 0; j < inputParamNames.size(); j++) //Write user defined params
                {
                    if (inputParamNames[j][0] != 'M')  //Couplings
                    {
                        lhcin << "set /Herwig/FRModel/FRModel:" << inputParamNames[j] << " " << inputParamValues[j] << endl;
                    }
                    else                            //Masses
                    {
                        inputParamNames[j].erase(0, 1);
                        lhcin << "set /Herwig/FRModel/Particles/" << inputParamNames[j] << ":NominalMass " << inputParamValues[j] << endl;
                    }
                }
                
                for (j = 0; j < paramNames.size(); j++) //Zero all left couplings
                {
                    usercontained = 0;
                    for (k = 0; k < inputParamNames.size(); k++)    //Check if they are not contained in inputParams
                    {
                        if (paramNames[j] == inputParamNames[k])
                        {
                            usercontained = 1;
                            break;
                        }
                    }
                    if (!usercontained)
                    {
                        for (k = 0; k < protectedParams.size(); k++) //Check if param is protected
                        {
                            if (paramNames[j] == protectedParams[k])
                            {
                                usercontained = 1;
                                break;
                            }
                        }
                    }
                    if (!usercontained)
                    {
                        lhcin << "set /Herwig/FRModel/FRModel:" << paramNames[j] << " " << "0" << endl;
                    }
                }
            }
        }
        lhcin.close();
    }
    else
    {
        printf("Error: Could not find .in file\n");
        return 0;
    }

    /*Cleanup*/
    inputParamNames.clear();
    inputParamValues.clear();
    paramNames.clear();

    lhcinBuf.clear();
    if (input.is_open())
    {
        input.close();
    }
    printf("Done\n");
    return 0;
}
