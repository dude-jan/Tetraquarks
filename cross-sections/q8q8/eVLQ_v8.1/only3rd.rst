(******************************************************************)
(*     Restriction file for eVLQ                                  *)
(*                                                                *)
(*     only couplings to 3rd gen particles                        *)
(******************************************************************)

M$Restrictions = {

            (* VLQs *)
            KTLw[i_?NumericQ] :> 0 /; (i =!= 3),
            KTLz[i_?NumericQ] :> 0 /; (i =!= 3),
            KTLh[i_?NumericQ] :> 0 /; (i =!= 3),
            KTRw[i_?NumericQ] :> 0 /; (i =!= 3),
            KTRz[i_?NumericQ] :> 0 /; (i =!= 3),
            KTRh[i_?NumericQ] :> 0 /; (i =!= 3),
            
            KBLw[i_?NumericQ] :> 0 /; (i =!= 3),
            KBLz[i_?NumericQ] :> 0 /; (i =!= 3),
            KBLh[i_?NumericQ] :> 0 /; (i =!= 3),
            KBRw[i_?NumericQ] :> 0 /; (i =!= 3),
            KBRz[i_?NumericQ] :> 0 /; (i =!= 3),
            KBRh[i_?NumericQ] :> 0 /; (i =!= 3),
            
            KXL[i_?NumericQ] :> 0 /; (i =!= 3),
            KXR[i_?NumericQ] :> 0 /; (i =!= 3),
            
            KYL[i_?NumericQ] :> 0 /; (i =!= 3),
            KYR[i_?NumericQ] :> 0 /; (i =!= 3),
            
            (* S10 *)
            KS10U[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            KS10D[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            KS10E[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            KS10N[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            
            KP10U[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            KP10D[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            KP10E[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            KP10N[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            
            
            KS10TL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS10TR[i_?NumericQ] :> 0 /; (i =!= 3),

            KS10BL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS10BR[i_?NumericQ] :> 0 /; (i =!= 3),

            (* S11 *)
            KS11qqL[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            KS11qqR[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
           
            KS11ll[i_?NumericQ, j_?NumericQ] :> 0 /; (i =!= 3 && j =!= 3),
            
            KS11TdL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS11TdR[i_?NumericQ] :> 0 /; (i =!= 3),

            KS11BuL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS11BuR[i_?NumericQ] :> 0 /; (i =!= 3),

            KS11XuL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS11XuR[i_?NumericQ] :> 0 /; (i =!= 3),

            KS11YdL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS11YdR[i_?NumericQ] :> 0 /; (i =!= 3),

            (* S12 *)
            KS12XDL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS12XDR[i_?NumericQ] :> 0 /; (i =!= 3),

            KS12YUL[i_?NumericQ] :> 0 /; (i =!= 3),
            KS12YUR[i_?NumericQ] :> 0 /; (i =!= 3)
            
            



}
