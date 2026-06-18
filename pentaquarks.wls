Needs["GroupMath`"]

(* ------------------------------------------------ *)
(* Basic definitions                                *)
(* ------------------------------------------------ *)


FormatRepName[repName_] := Replace[repName, {
  OverBar[x_] :> ToString[x] <> "bar",
  other_ :> ToString[other]
}]

SingletQ[rep_List] := VectorQ[rep, # === 0 &];

SingletMultiplicity[group_, reps_List] :=
 Module[{dec},
  dec = ReduceRepProduct[group, reps];
  Total[Cases[dec, {rep_?SingletQ, mult_} :> mult]]
 ]

(* ------------------------------------------------ *)
(* Generate all proper bipartitions                 *)
(* ------------------------------------------------ *)

ProperBipartitions[list_] :=
 Module[{n = Length[list], subs},
  subs = Rest[Most[Subsets[Range[n]]]];
  DeleteDuplicatesBy[
   Select[subs, Length[#] <= n/2 &],
   Sort[{#, Complement[Range[n], #]}] &
   ]
 ]

(* ------------------------------------------------ *)
(* Number of factorized singlets                    *)
(* ------------------------------------------------ *)

FactorizedSinglets[group_, reps_List] :=
 Module[
  {parts, count = 0, left, right, ml, mr},

  parts = ProperBipartitions[reps];

  Do[
   left = reps[[part]];
   right = reps[[Complement[Range[Length[reps]], part]]];

   ml = SingletMultiplicity[group, left];
   mr = SingletMultiplicity[group, right];

   count += ml*mr;

   ,
   {part, parts}
   ];

  count
 ]

(* ------------------------------------------------ *)
(* Primitive singlets estimate                      *)
(* ------------------------------------------------ *)

PrimitiveSinglets[group_, reps_List] :=
 Module[
  {full, fact},

  full = SingletMultiplicity[group, reps];
  fact = FactorizedSinglets[group, reps];

  <|
   "TotalSinglets" -> full,
   "FactorizedSinglets" -> fact,
   "PrimitiveSinglets" -> Max[0, full - fact]
   |>
 ]


(* ------------------------------------------------ *)
(* Find all combinations of 5 representations containing singlets *)
(* ------------------------------------------------ *)

FindPentaquarkSinglets[group_, reps_List] :=
 Module[{rawReps, namesMap, combs, res, displayComb, resList, displayCombs, combStrings, maxW},
  If[AllTrue[reps, Head[#] === Rule &],
   If[ListQ[reps[[1, 2]]],
    rawReps = reps[[All, 2]];
    namesMap = Map[#[[2]] -> #[[1]] &, reps];
    ,
    rawReps = reps[[All, 1]];
    namesMap = reps;
   ]
   ,
   rawReps = reps;
   namesMap = Map[# -> FormatRepName[RepName[group, #]] &, reps];
  ];
  combs = DeleteDuplicates[Sort /@ Tuples[rawReps, 5]];
  resList = {};
  displayCombs = {};
  combStrings = {};
  Do[
   res = PrimitiveSinglets[group, comb];
   If[res["TotalSinglets"] > 0,
    displayComb = comb /. namesMap;
    AppendTo[resList, res];
    AppendTo[displayCombs, displayComb];
    AppendTo[combStrings, ToString[displayComb]];
   ],
   {comb, combs}
  ];
  
  If[Length[resList] > 0,
   maxW = Max[Map[StringLength, combStrings]];
   Do[
    Print[
     StringPadRight[combStrings[[i]], maxW], 
     " -> ", 
     "Singlets: ", 
     resList[[i]]["FactorizedSinglets"], 
     " factorized and ", 
     resList[[i]]["PrimitiveSinglets"], 
     " primitive"
    ],
    {i, 1, Length[resList]}
   ]
  ]
 ]

SetAttributes[RunModel, HoldAll];
RunModel[name_String, group_, reps_List] := Module[{evalGroup, evalReps},
  evalGroup = group;
  evalReps = reps;
  Print["\n=== ", name, " ==="];
  Print["Group: ", ToString[Unevaluated[group]]];
  If[AllTrue[evalReps, Head[#] === Rule &],
   If[ListQ[evalReps[[1, 2]]],
    Print["Irreps: ", StringRiffle[Table[r[[1]] <> " = " <> FormatRepName[RepName[evalGroup, r[[2]]]], {r, evalReps}], ", "]];
    ,
    Print["Irreps: ", StringRiffle[Table[r[[2]] <> " = " <> FormatRepName[RepName[evalGroup, r[[1]]]], {r, evalReps}], ", "]];
   ]
   ,
   Print["Irreps: ", StringRiffle[Table[FormatRepName[RepName[evalGroup, r]], {r, evalReps}], ", "]];
  ];
  FindPentaquarkSinglets[evalGroup, evalReps]
]

(* Model M1 *)
psiM1 = {1, 0, 0};
chiM1 = {0, 0, 1};
RunModel["Model M1", SO7, {psiM1 -> "psi", chiM1 -> "chi"}]

(* Model M2 *)
psiM2 = {1, 0, 0, 0};
chiM2 = {0, 0, 0, 1};
RunModel["Model M2", SO9, {psiM2 -> "psi", chiM2 -> "chi"}]

(* Model M3 *)
psiM3 = {0, 0, 1};
chiM3 = {1, 0, 0};
RunModel["Model M3", SO7, {psiM3 -> "psi", chiM3 -> "chi"}]

(* Model M4 *)
psiM4 = {0, 0, 0, 1};
chiM4 = {1, 0, 0, 0};
RunModel["Model M4", SO9, {psiM4 -> "psi", chiM4 -> "chi"}]

(* Model M5 *)
psiM5 = {0, 1};
chiM5 = {1, 0};
RunModel["Model M5", Sp4, {psiM5 -> "psi", chiM5 -> "chi"}]

(* Model M6 *)
psiM6 = {0, 1, 0};
chiM6 = {1, 0, 0};
chibarM6 = {0, 0, 1};
RunModel["Model M6", SU4, {psiM6 -> "psi", chiM6 -> "chi", chibarM6 -> "chibar"}]

(* Model M7 *)
psiM7 = {1, 0, 0, 0, 0};
chiM7 = {0, 0, 0, 0, 1};
chibarM7 = {0, 0, 0, 1, 0};
RunModel["Model M7", SO10, {psiM7 -> "psi", chiM7 -> "chi", chibarM7 -> "chibar"}]

(* Model M8 *)
psiM8 = {1, 0};
chiM8 = {0, 1};
RunModel["Model M8", Sp4, {psiM8 -> "psi", chiM8 -> "chi"}]

(* Model M9 *)
psiM9 = {0, 0, 0, 0, 1};
chiM9 = {1, 0, 0, 0, 0};
RunModel["Model M9", SO11, {psiM9 -> "psi", chiM9 -> "chi"}]

(* Model M10 *)
psiM10 = {0, 0, 0, 0, 1};
psibarM10 = {0, 0, 0, 1, 0};
chiM10 = {1, 0, 0, 0, 0};
RunModel["Model M10", SO10, {psiM10 -> "psi", psibarM10 -> "psibar", chiM10 -> "chi"}]

(* Model M11 *)
psiM11 = {1, 0, 0};
psibarM11 = {0, 0, 1};
chiM11 = {0, 1, 0};
RunModel["Model M11", SU4, {psiM11 -> "psi", psibarM11 -> "psibar", chiM11 -> "chi"}]

(* Model M12 *)
psiM12 = {1, 0, 0, 0};
psibarM12 = {0, 0, 0, 1};
chiM12 = {0, 1, 0, 0};
chibarM12 = {0, 0, 1, 0};
RunModel["Model M12", SU5, {psiM12 -> "psi", psibarM12 -> "psibar", chiM12 -> "chi", chibarM12 -> "chibar"}]