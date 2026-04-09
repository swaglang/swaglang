# Generated from grammar/SwagLangParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,58,463,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,5,1,76,8,1,10,1,12,1,79,9,1,1,
        2,1,2,1,3,1,3,1,3,3,3,86,8,3,1,4,1,4,1,4,1,4,5,4,92,8,4,10,4,12,
        4,95,9,4,1,4,1,4,1,5,3,5,100,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,112,8,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,5,9,123,
        8,9,10,9,12,9,126,9,9,3,9,128,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        5,10,136,8,10,10,10,12,10,139,9,10,1,10,3,10,142,8,10,3,10,144,8,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,4,11,155,8,11,11,
        11,12,11,156,1,11,1,11,3,11,161,8,11,1,12,1,12,1,12,5,12,166,8,12,
        10,12,12,12,169,9,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,177,8,13,
        10,13,12,13,180,9,13,3,13,182,8,13,1,13,1,13,5,13,186,8,13,10,13,
        12,13,189,9,13,1,13,1,13,4,13,193,8,13,11,13,12,13,194,1,13,5,13,
        198,8,13,10,13,12,13,201,9,13,1,13,5,13,204,8,13,10,13,12,13,207,
        9,13,3,13,209,8,13,1,13,1,13,1,14,1,14,3,14,215,8,14,1,14,1,14,1,
        14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,226,8,15,1,16,1,16,1,16,1,
        16,5,16,232,8,16,10,16,12,16,235,9,16,1,16,3,16,238,8,16,3,16,240,
        8,16,1,16,1,16,1,17,1,17,5,17,246,8,17,10,17,12,17,249,9,17,1,17,
        1,17,1,17,5,17,254,8,17,10,17,12,17,257,9,17,1,17,5,17,260,8,17,
        10,17,12,17,263,9,17,1,17,3,17,266,8,17,3,17,268,8,17,1,17,5,17,
        271,8,17,10,17,12,17,274,9,17,1,17,1,17,1,18,1,18,1,18,3,18,281,
        8,18,1,18,1,18,1,18,1,19,1,19,1,19,3,19,289,8,19,1,19,1,19,1,19,
        5,19,294,8,19,10,19,12,19,297,9,19,1,20,1,20,1,20,1,20,3,20,303,
        8,20,1,20,1,20,1,20,1,20,1,20,1,20,4,20,311,8,20,11,20,12,20,312,
        1,20,1,20,3,20,317,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,4,21,
        326,8,21,11,21,12,21,327,1,21,1,21,1,21,3,21,333,8,21,1,22,1,22,
        1,23,1,23,1,24,1,24,1,24,3,24,342,8,24,1,25,1,25,1,25,1,25,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,3,27,357,8,27,1,27,1,27,
        3,27,361,8,27,1,27,1,27,3,27,365,8,27,1,27,3,27,368,8,27,1,27,1,
        27,1,28,1,28,1,28,1,28,1,28,3,28,377,8,28,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,5,29,386,8,29,10,29,12,29,389,9,29,1,29,1,29,3,29,393,
        8,29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,3,31,410,8,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,5,31,436,8,31,10,31,12,31,439,9,31,1,32,1,32,
        1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,5,34,453,8,34,
        10,34,12,34,456,9,34,1,34,3,34,459,8,34,3,34,461,8,34,1,34,0,1,62,
        35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,0,7,2,0,4,4,17,17,1,0,52,
        53,1,0,29,34,1,0,42,43,1,0,39,41,1,0,50,51,1,0,44,49,506,0,70,1,
        0,0,0,2,77,1,0,0,0,4,80,1,0,0,0,6,85,1,0,0,0,8,87,1,0,0,0,10,99,
        1,0,0,0,12,111,1,0,0,0,14,113,1,0,0,0,16,116,1,0,0,0,18,118,1,0,
        0,0,20,129,1,0,0,0,22,160,1,0,0,0,24,162,1,0,0,0,26,170,1,0,0,0,
        28,212,1,0,0,0,30,225,1,0,0,0,32,227,1,0,0,0,34,243,1,0,0,0,36,277,
        1,0,0,0,38,285,1,0,0,0,40,316,1,0,0,0,42,332,1,0,0,0,44,334,1,0,
        0,0,46,336,1,0,0,0,48,341,1,0,0,0,50,343,1,0,0,0,52,347,1,0,0,0,
        54,367,1,0,0,0,56,371,1,0,0,0,58,378,1,0,0,0,60,394,1,0,0,0,62,409,
        1,0,0,0,64,440,1,0,0,0,66,445,1,0,0,0,68,460,1,0,0,0,70,71,3,2,1,
        0,71,72,5,0,0,1,72,1,1,0,0,0,73,76,3,4,2,0,74,76,5,55,0,0,75,73,
        1,0,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,
        78,3,1,0,0,0,79,77,1,0,0,0,80,81,3,6,3,0,81,5,1,0,0,0,82,86,3,20,
        10,0,83,86,3,40,20,0,84,86,3,26,13,0,85,82,1,0,0,0,85,83,1,0,0,0,
        85,84,1,0,0,0,86,7,1,0,0,0,87,93,5,22,0,0,88,89,3,10,5,0,89,90,5,
        55,0,0,90,92,1,0,0,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,
        94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,23,0,0,97,9,1,0,0,
        0,98,100,3,12,6,0,99,98,1,0,0,0,99,100,1,0,0,0,100,11,1,0,0,0,101,
        112,3,20,10,0,102,112,3,42,21,0,103,112,3,64,32,0,104,112,3,40,20,
        0,105,112,3,48,24,0,106,112,3,58,29,0,107,112,3,16,8,0,108,112,3,
        18,9,0,109,112,3,14,7,0,110,112,3,62,31,0,111,101,1,0,0,0,111,102,
        1,0,0,0,111,103,1,0,0,0,111,104,1,0,0,0,111,105,1,0,0,0,111,106,
        1,0,0,0,111,107,1,0,0,0,111,108,1,0,0,0,111,109,1,0,0,0,111,110,
        1,0,0,0,112,13,1,0,0,0,113,114,5,14,0,0,114,115,3,62,31,0,115,15,
        1,0,0,0,116,117,5,12,0,0,117,17,1,0,0,0,118,127,5,13,0,0,119,124,
        3,62,31,0,120,121,5,27,0,0,121,123,3,62,31,0,122,120,1,0,0,0,123,
        126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,128,1,0,0,0,126,
        124,1,0,0,0,127,119,1,0,0,0,127,128,1,0,0,0,128,19,1,0,0,0,129,130,
        3,22,11,0,130,131,5,17,0,0,131,143,5,20,0,0,132,137,3,66,33,0,133,
        134,5,27,0,0,134,136,3,66,33,0,135,133,1,0,0,0,136,139,1,0,0,0,137,
        135,1,0,0,0,137,138,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,140,
        142,5,27,0,0,141,140,1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,
        132,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,5,21,0,0,146,
        147,3,8,4,0,147,21,1,0,0,0,148,161,3,24,12,0,149,161,5,3,0,0,150,
        151,5,20,0,0,151,154,3,24,12,0,152,153,5,27,0,0,153,155,3,24,12,
        0,154,152,1,0,0,0,155,156,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,
        0,157,158,1,0,0,0,158,159,5,21,0,0,159,161,1,0,0,0,160,148,1,0,0,
        0,160,149,1,0,0,0,160,150,1,0,0,0,161,23,1,0,0,0,162,167,7,0,0,0,
        163,164,5,24,0,0,164,166,5,25,0,0,165,163,1,0,0,0,166,169,1,0,0,
        0,167,165,1,0,0,0,167,168,1,0,0,0,168,25,1,0,0,0,169,167,1,0,0,0,
        170,171,5,1,0,0,171,181,5,17,0,0,172,173,5,2,0,0,173,178,5,17,0,
        0,174,175,5,27,0,0,175,177,5,17,0,0,176,174,1,0,0,0,177,180,1,0,
        0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,182,1,0,0,0,180,178,1,0,
        0,0,181,172,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,187,5,22,
        0,0,184,186,5,55,0,0,185,184,1,0,0,0,186,189,1,0,0,0,187,185,1,0,
        0,0,187,188,1,0,0,0,188,208,1,0,0,0,189,187,1,0,0,0,190,199,3,28,
        14,0,191,193,5,55,0,0,192,191,1,0,0,0,193,194,1,0,0,0,194,192,1,
        0,0,0,194,195,1,0,0,0,195,196,1,0,0,0,196,198,3,28,14,0,197,192,
        1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,205,
        1,0,0,0,201,199,1,0,0,0,202,204,5,55,0,0,203,202,1,0,0,0,204,207,
        1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,205,
        1,0,0,0,208,190,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,211,
        5,23,0,0,211,27,1,0,0,0,212,214,5,17,0,0,213,215,5,26,0,0,214,213,
        1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,0,216,217,5,18,0,0,217,218,
        3,24,12,0,218,29,1,0,0,0,219,226,5,53,0,0,220,226,5,52,0,0,221,226,
        5,54,0,0,222,226,5,16,0,0,223,226,3,32,16,0,224,226,3,34,17,0,225,
        219,1,0,0,0,225,220,1,0,0,0,225,221,1,0,0,0,225,222,1,0,0,0,225,
        223,1,0,0,0,225,224,1,0,0,0,226,31,1,0,0,0,227,239,5,24,0,0,228,
        233,3,30,15,0,229,230,5,27,0,0,230,232,3,30,15,0,231,229,1,0,0,0,
        232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,237,1,0,0,0,
        235,233,1,0,0,0,236,238,5,27,0,0,237,236,1,0,0,0,237,238,1,0,0,0,
        238,240,1,0,0,0,239,228,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,
        241,242,5,25,0,0,242,33,1,0,0,0,243,247,5,22,0,0,244,246,5,55,0,
        0,245,244,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,
        0,248,267,1,0,0,0,249,247,1,0,0,0,250,261,3,36,18,0,251,255,5,27,
        0,0,252,254,5,55,0,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,
        0,0,255,256,1,0,0,0,256,258,1,0,0,0,257,255,1,0,0,0,258,260,3,36,
        18,0,259,251,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,
        0,0,262,265,1,0,0,0,263,261,1,0,0,0,264,266,5,27,0,0,265,264,1,0,
        0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,250,1,0,0,0,267,268,1,0,
        0,0,268,272,1,0,0,0,269,271,5,55,0,0,270,269,1,0,0,0,271,274,1,0,
        0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,275,1,0,0,0,274,272,1,0,
        0,0,275,276,5,23,0,0,276,35,1,0,0,0,277,280,5,17,0,0,278,279,5,18,
        0,0,279,281,3,24,12,0,280,278,1,0,0,0,280,281,1,0,0,0,281,282,1,
        0,0,0,282,283,5,29,0,0,283,284,3,62,31,0,284,37,1,0,0,0,285,295,
        5,17,0,0,286,288,5,24,0,0,287,289,7,1,0,0,288,287,1,0,0,0,288,289,
        1,0,0,0,289,290,1,0,0,0,290,294,5,25,0,0,291,292,5,28,0,0,292,294,
        3,38,19,0,293,286,1,0,0,0,293,291,1,0,0,0,294,297,1,0,0,0,295,293,
        1,0,0,0,295,296,1,0,0,0,296,39,1,0,0,0,297,295,1,0,0,0,298,299,5,
        15,0,0,299,302,5,17,0,0,300,301,5,18,0,0,301,303,3,24,12,0,302,300,
        1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,5,29,0,0,305,317,
        3,62,31,0,306,307,5,15,0,0,307,310,5,17,0,0,308,309,5,27,0,0,309,
        311,5,17,0,0,310,308,1,0,0,0,311,312,1,0,0,0,312,310,1,0,0,0,312,
        313,1,0,0,0,313,314,1,0,0,0,314,315,5,29,0,0,315,317,3,64,32,0,316,
        298,1,0,0,0,316,306,1,0,0,0,317,41,1,0,0,0,318,319,3,38,19,0,319,
        320,7,2,0,0,320,321,3,62,31,0,321,333,1,0,0,0,322,325,3,38,19,0,
        323,324,5,27,0,0,324,326,3,38,19,0,325,323,1,0,0,0,326,327,1,0,0,
        0,327,325,1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,0,329,330,5,29,0,
        0,330,331,3,64,32,0,331,333,1,0,0,0,332,318,1,0,0,0,332,322,1,0,
        0,0,333,43,1,0,0,0,334,335,3,8,4,0,335,45,1,0,0,0,336,337,3,8,4,
        0,337,47,1,0,0,0,338,342,3,54,27,0,339,342,3,50,25,0,340,342,3,52,
        26,0,341,338,1,0,0,0,341,339,1,0,0,0,341,340,1,0,0,0,342,49,1,0,
        0,0,343,344,5,10,0,0,344,345,3,60,30,0,345,346,3,46,23,0,346,51,
        1,0,0,0,347,348,5,11,0,0,348,349,3,46,23,0,349,350,5,10,0,0,350,
        351,5,20,0,0,351,352,3,60,30,0,352,353,5,21,0,0,353,53,1,0,0,0,354,
        356,5,8,0,0,355,357,3,36,18,0,356,355,1,0,0,0,356,357,1,0,0,0,357,
        358,1,0,0,0,358,360,5,19,0,0,359,361,3,60,30,0,360,359,1,0,0,0,360,
        361,1,0,0,0,361,362,1,0,0,0,362,364,5,19,0,0,363,365,3,62,31,0,364,
        363,1,0,0,0,364,365,1,0,0,0,365,368,1,0,0,0,366,368,3,56,28,0,367,
        354,1,0,0,0,367,366,1,0,0,0,368,369,1,0,0,0,369,370,3,46,23,0,370,
        55,1,0,0,0,371,372,5,8,0,0,372,373,5,17,0,0,373,376,5,9,0,0,374,
        377,3,64,32,0,375,377,3,38,19,0,376,374,1,0,0,0,376,375,1,0,0,0,
        377,57,1,0,0,0,378,379,5,5,0,0,379,380,3,60,30,0,380,387,3,44,22,
        0,381,382,5,6,0,0,382,383,3,60,30,0,383,384,3,44,22,0,384,386,1,
        0,0,0,385,381,1,0,0,0,386,389,1,0,0,0,387,385,1,0,0,0,387,388,1,
        0,0,0,388,392,1,0,0,0,389,387,1,0,0,0,390,391,5,7,0,0,391,393,3,
        44,22,0,392,390,1,0,0,0,392,393,1,0,0,0,393,59,1,0,0,0,394,395,3,
        62,31,0,395,61,1,0,0,0,396,397,6,31,-1,0,397,398,5,20,0,0,398,399,
        3,62,31,0,399,400,5,21,0,0,400,410,1,0,0,0,401,410,3,30,15,0,402,
        410,3,64,32,0,403,410,3,38,19,0,404,405,3,38,19,0,405,406,7,3,0,
        0,406,410,1,0,0,0,407,408,5,37,0,0,408,410,3,62,31,8,409,396,1,0,
        0,0,409,401,1,0,0,0,409,402,1,0,0,0,409,403,1,0,0,0,409,404,1,0,
        0,0,409,407,1,0,0,0,410,437,1,0,0,0,411,412,10,7,0,0,412,413,5,38,
        0,0,413,436,3,62,31,7,414,415,10,6,0,0,415,416,7,4,0,0,416,436,3,
        62,31,7,417,418,10,5,0,0,418,419,7,5,0,0,419,436,3,62,31,6,420,421,
        10,4,0,0,421,422,7,6,0,0,422,436,3,62,31,5,423,424,10,3,0,0,424,
        425,5,35,0,0,425,436,3,62,31,4,426,427,10,2,0,0,427,428,5,36,0,0,
        428,436,3,62,31,3,429,430,10,1,0,0,430,431,5,26,0,0,431,432,3,62,
        31,0,432,433,5,18,0,0,433,434,3,62,31,2,434,436,1,0,0,0,435,411,
        1,0,0,0,435,414,1,0,0,0,435,417,1,0,0,0,435,420,1,0,0,0,435,423,
        1,0,0,0,435,426,1,0,0,0,435,429,1,0,0,0,436,439,1,0,0,0,437,435,
        1,0,0,0,437,438,1,0,0,0,438,63,1,0,0,0,439,437,1,0,0,0,440,441,5,
        17,0,0,441,442,5,20,0,0,442,443,3,68,34,0,443,444,5,21,0,0,444,65,
        1,0,0,0,445,446,5,17,0,0,446,447,5,18,0,0,447,448,3,24,12,0,448,
        67,1,0,0,0,449,454,3,62,31,0,450,451,5,27,0,0,451,453,3,62,31,0,
        452,450,1,0,0,0,453,456,1,0,0,0,454,452,1,0,0,0,454,455,1,0,0,0,
        455,458,1,0,0,0,456,454,1,0,0,0,457,459,5,27,0,0,458,457,1,0,0,0,
        458,459,1,0,0,0,459,461,1,0,0,0,460,449,1,0,0,0,460,461,1,0,0,0,
        461,69,1,0,0,0,55,75,77,85,93,99,111,124,127,137,141,143,156,160,
        167,178,181,187,194,199,205,208,214,225,233,237,239,247,255,261,
        265,267,272,280,288,293,295,302,312,316,327,332,341,356,360,364,
        367,376,387,392,409,435,437,454,458,460
    ]

class SwagLangParser ( Parser ):

    grammarFileName = "SwagLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'interface'", "'extends'", "'void'", 
                     "<INVALID>", "'if'", "<INVALID>", "'else'", "'for'", 
                     "'in'", "'while'", "'do'", "'break'", "'return'", "'defer'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'", "';'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "'?'", "','", 
                     "'.'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'&&'", "'||'", "'!'", "'**'", "'*'", "'/'", "'%'", 
                     "'++'", "'--'", "'>'", "'<'", "'=='", "'!='", "'>='", 
                     "'<='", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INTERFACE", "EXTENDS", "VOID", "TYPE", 
                      "IF", "ELSE_IF", "ELSE", "FOR", "IN", "WHILE", "DO", 
                      "BREAK", "RETURN", "DEFER", "ACCESS_MOD", "BOOL", 
                      "IDENT", "COLUMN", "SEMICOL", "L_PAREN", "R_PAREN", 
                      "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "QUESTION", 
                      "COMMA", "DOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND", "OR", 
                      "NOT", "EXP", "MUL", "DIV", "MOD", "INC", "DEC", "GT", 
                      "LT", "EQ", "NEQ", "GTE", "LTE", "PLUS", "MINUS", 
                      "STRING", "INT", "FLOAT", "NWLN", "SPACE", "COMMENT", 
                      "INLINE_COMMENT" ]

    RULE_prog = 0
    RULE_stmts = 1
    RULE_stmt = 2
    RULE_pure_stmt = 3
    RULE_code_block = 4
    RULE_func_stmt = 5
    RULE_pure_func_stmt = 6
    RULE_defer = 7
    RULE_break = 8
    RULE_return = 9
    RULE_func_decl = 10
    RULE_return_type = 11
    RULE_type_ann = 12
    RULE_interface_decl = 13
    RULE_interface_field = 14
    RULE_data = 15
    RULE_list = 16
    RULE_dict = 17
    RULE_no_acs_mode_var_decl = 18
    RULE_var_ref = 19
    RULE_var_decl = 20
    RULE_var_assign = 21
    RULE_conditional_body = 22
    RULE_loop_body = 23
    RULE_loop = 24
    RULE_while_loop = 25
    RULE_do_while_loop = 26
    RULE_for_loop = 27
    RULE_forin = 28
    RULE_conditional = 29
    RULE_condition = 30
    RULE_expr = 31
    RULE_func_call = 32
    RULE_param_decl = 33
    RULE_params = 34

    ruleNames =  [ "prog", "stmts", "stmt", "pure_stmt", "code_block", "func_stmt", 
                   "pure_func_stmt", "defer", "break", "return", "func_decl", 
                   "return_type", "type_ann", "interface_decl", "interface_field", 
                   "data", "list", "dict", "no_acs_mode_var_decl", "var_ref", 
                   "var_decl", "var_assign", "conditional_body", "loop_body", 
                   "loop", "while_loop", "do_while_loop", "for_loop", "forin", 
                   "conditional", "condition", "expr", "func_call", "param_decl", 
                   "params" ]

    EOF = Token.EOF
    INTERFACE=1
    EXTENDS=2
    VOID=3
    TYPE=4
    IF=5
    ELSE_IF=6
    ELSE=7
    FOR=8
    IN=9
    WHILE=10
    DO=11
    BREAK=12
    RETURN=13
    DEFER=14
    ACCESS_MOD=15
    BOOL=16
    IDENT=17
    COLUMN=18
    SEMICOL=19
    L_PAREN=20
    R_PAREN=21
    L_CURLY=22
    R_CURLY=23
    L_BRACKET=24
    R_BRACKET=25
    QUESTION=26
    COMMA=27
    DOT=28
    ASSIGN=29
    ADD_ASSIGN=30
    SUB_ASSIGN=31
    MUL_ASSIGN=32
    DIV_ASSIGN=33
    MOD_ASSIGN=34
    AND=35
    OR=36
    NOT=37
    EXP=38
    MUL=39
    DIV=40
    MOD=41
    INC=42
    DEC=43
    GT=44
    LT=45
    EQ=46
    NEQ=47
    GTE=48
    LTE=49
    PLUS=50
    MINUS=51
    STRING=52
    INT=53
    FLOAT=54
    NWLN=55
    SPACE=56
    COMMENT=57
    INLINE_COMMENT=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmts(self):
            return self.getTypedRuleContext(SwagLangParser.StmtsContext,0)


        def EOF(self):
            return self.getToken(SwagLangParser.EOF, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SwagLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.stmts()
            self.state = 71
            self.match(SwagLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.StmtContext,i)


        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = SwagLangParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028797020176410) != 0):
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 4, 15, 17, 20]:
                    self.state = 73
                    self.stmt()
                    pass
                elif token in [55]:
                    self.state = 74
                    self.match(SwagLangParser.NWLN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pure_stmt(self):
            return self.getTypedRuleContext(SwagLangParser.Pure_stmtContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = SwagLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.pure_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pure_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Func_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Var_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Interface_declContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_pure_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPure_stmt" ):
                listener.enterPure_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPure_stmt" ):
                listener.exitPure_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPure_stmt" ):
                return visitor.visitPure_stmt(self)
            else:
                return visitor.visitChildren(self)




    def pure_stmt(self):

        localctx = SwagLangParser.Pure_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pure_stmt)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 17, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.func_decl()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.var_decl()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.interface_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(SwagLangParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(SwagLangParser.R_CURLY, 0)

        def func_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Func_stmtContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Func_stmtContext,i)


        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = SwagLangParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SwagLangParser.L_CURLY)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67554131871792440) != 0):
                self.state = 88
                self.func_stmt()
                self.state = 89
                self.match(SwagLangParser.NWLN)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(SwagLangParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pure_func_stmt(self):
            return self.getTypedRuleContext(SwagLangParser.Pure_func_stmtContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_func_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_stmt" ):
                listener.enterFunc_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_stmt" ):
                listener.exitFunc_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_stmt" ):
                return visitor.visitFunc_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_stmt(self):

        localctx = SwagLangParser.Func_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525334852828472) != 0):
                self.state = 98
                self.pure_func_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pure_func_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Func_declContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(SwagLangParser.Var_assignContext,0)


        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(SwagLangParser.Var_declContext,0)


        def loop(self):
            return self.getTypedRuleContext(SwagLangParser.LoopContext,0)


        def conditional(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionalContext,0)


        def break_(self):
            return self.getTypedRuleContext(SwagLangParser.BreakContext,0)


        def return_(self):
            return self.getTypedRuleContext(SwagLangParser.ReturnContext,0)


        def defer(self):
            return self.getTypedRuleContext(SwagLangParser.DeferContext,0)


        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_pure_func_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPure_func_stmt" ):
                listener.enterPure_func_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPure_func_stmt" ):
                listener.exitPure_func_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPure_func_stmt" ):
                return visitor.visitPure_func_stmt(self)
            else:
                return visitor.visitChildren(self)




    def pure_func_stmt(self):

        localctx = SwagLangParser.Pure_func_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pure_func_stmt)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.var_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.var_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                self.loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 106
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 107
                self.break_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 108
                self.return_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 109
                self.defer()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 110
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeferContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFER(self):
            return self.getToken(SwagLangParser.DEFER, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_defer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefer" ):
                listener.enterDefer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefer" ):
                listener.exitDefer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefer" ):
                return visitor.visitDefer(self)
            else:
                return visitor.visitChildren(self)




    def defer(self):

        localctx = SwagLangParser.DeferContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_defer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(SwagLangParser.DEFER)
            self.state = 114
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(SwagLangParser.BREAK, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = SwagLangParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(SwagLangParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SwagLangParser.RETURN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = SwagLangParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(SwagLangParser.RETURN)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525334852763648) != 0):
                self.state = 119
                self.expr(0)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 120
                    self.match(SwagLangParser.COMMA)
                    self.state = 121
                    self.expr(0)
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(SwagLangParser.Return_typeContext,0)


        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def code_block(self):
            return self.getTypedRuleContext(SwagLangParser.Code_blockContext,0)


        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Param_declContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Param_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = SwagLangParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.return_type()
            self.state = 130
            self.match(SwagLangParser.IDENT)
            self.state = 131
            self.match(SwagLangParser.L_PAREN)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 132
                self.param_decl()
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 133
                        self.match(SwagLangParser.COMMA)
                        self.state = 134
                        self.param_decl() 
                    self.state = 139
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 140
                    self.match(SwagLangParser.COMMA)




            self.state = 145
            self.match(SwagLangParser.R_PAREN)
            self.state = 146
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_ann(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Type_annContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Type_annContext,i)


        def VOID(self):
            return self.getToken(SwagLangParser.VOID, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = SwagLangParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return_type)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.type_ann()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(SwagLangParser.VOID)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(SwagLangParser.L_PAREN)
                self.state = 151
                self.type_ann()
                self.state = 154 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 152
                    self.match(SwagLangParser.COMMA)
                    self.state = 153
                    self.type_ann()
                    self.state = 156 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==27):
                        break

                self.state = 158
                self.match(SwagLangParser.R_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_annContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(SwagLangParser.TYPE, 0)

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def L_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.L_BRACKET)
            else:
                return self.getToken(SwagLangParser.L_BRACKET, i)

        def R_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.R_BRACKET)
            else:
                return self.getToken(SwagLangParser.R_BRACKET, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_type_ann

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_ann" ):
                listener.enterType_ann(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_ann" ):
                listener.exitType_ann(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_ann" ):
                return visitor.visitType_ann(self)
            else:
                return visitor.visitChildren(self)




    def type_ann(self):

        localctx = SwagLangParser.Type_annContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_ann)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not(_la==4 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 163
                self.match(SwagLangParser.L_BRACKET)
                self.state = 164
                self.match(SwagLangParser.R_BRACKET)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(SwagLangParser.INTERFACE, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.IDENT)
            else:
                return self.getToken(SwagLangParser.IDENT, i)

        def L_CURLY(self):
            return self.getToken(SwagLangParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(SwagLangParser.R_CURLY, 0)

        def EXTENDS(self):
            return self.getToken(SwagLangParser.EXTENDS, 0)

        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def interface_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Interface_fieldContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Interface_fieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_interface_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_decl" ):
                listener.enterInterface_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_decl" ):
                listener.exitInterface_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = SwagLangParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(SwagLangParser.INTERFACE)
            self.state = 171
            self.match(SwagLangParser.IDENT)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 172
                self.match(SwagLangParser.EXTENDS)
                self.state = 173
                self.match(SwagLangParser.IDENT)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 174
                    self.match(SwagLangParser.COMMA)
                    self.state = 175
                    self.match(SwagLangParser.IDENT)
                    self.state = 180
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 183
            self.match(SwagLangParser.L_CURLY)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 184
                self.match(SwagLangParser.NWLN)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 190
                self.interface_field()
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 192 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 191
                            self.match(SwagLangParser.NWLN)
                            self.state = 194 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==55):
                                break

                        self.state = 196
                        self.interface_field() 
                    self.state = 201
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 202
                    self.match(SwagLangParser.NWLN)
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 210
            self.match(SwagLangParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def type_ann(self):
            return self.getTypedRuleContext(SwagLangParser.Type_annContext,0)


        def QUESTION(self):
            return self.getToken(SwagLangParser.QUESTION, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_interface_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterface_field" ):
                listener.enterInterface_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterface_field" ):
                listener.exitInterface_field(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_field" ):
                return visitor.visitInterface_field(self)
            else:
                return visitor.visitChildren(self)




    def interface_field(self):

        localctx = SwagLangParser.Interface_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(SwagLangParser.IDENT)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 213
                self.match(SwagLangParser.QUESTION)


            self.state = 216
            self.match(SwagLangParser.COLUMN)
            self.state = 217
            self.type_ann()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SwagLangParser.INT, 0)

        def STRING(self):
            return self.getToken(SwagLangParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(SwagLangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(SwagLangParser.BOOL, 0)

        def list_(self):
            return self.getTypedRuleContext(SwagLangParser.ListContext,0)


        def dict_(self):
            return self.getTypedRuleContext(SwagLangParser.DictContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = SwagLangParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_data)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(SwagLangParser.INT)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(SwagLangParser.STRING)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(SwagLangParser.FLOAT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(SwagLangParser.BOOL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.list_()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
                self.dict_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(SwagLangParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(SwagLangParser.R_BRACKET, 0)

        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.DataContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.DataContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = SwagLangParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(SwagLangParser.L_BRACKET)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525197412630528) != 0):
                self.state = 228
                self.data()
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 229
                        self.match(SwagLangParser.COMMA)
                        self.state = 230
                        self.data() 
                    self.state = 235
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 236
                    self.match(SwagLangParser.COMMA)




            self.state = 241
            self.match(SwagLangParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(SwagLangParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(SwagLangParser.R_CURLY, 0)

        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def no_acs_mode_var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.No_acs_mode_var_declContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.No_acs_mode_var_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDict" ):
                listener.enterDict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDict" ):
                listener.exitDict(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict" ):
                return visitor.visitDict(self)
            else:
                return visitor.visitChildren(self)




    def dict_(self):

        localctx = SwagLangParser.DictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dict)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(SwagLangParser.L_CURLY)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 244
                    self.match(SwagLangParser.NWLN) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 250
                self.no_acs_mode_var_decl()
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 251
                        self.match(SwagLangParser.COMMA)
                        self.state = 255
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==55:
                            self.state = 252
                            self.match(SwagLangParser.NWLN)
                            self.state = 257
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 258
                        self.no_acs_mode_var_decl() 
                    self.state = 263
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 264
                    self.match(SwagLangParser.COMMA)




            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 269
                self.match(SwagLangParser.NWLN)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 275
            self.match(SwagLangParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class No_acs_mode_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def ASSIGN(self):
            return self.getToken(SwagLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def type_ann(self):
            return self.getTypedRuleContext(SwagLangParser.Type_annContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_no_acs_mode_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNo_acs_mode_var_decl" ):
                listener.enterNo_acs_mode_var_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNo_acs_mode_var_decl" ):
                listener.exitNo_acs_mode_var_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNo_acs_mode_var_decl" ):
                return visitor.visitNo_acs_mode_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def no_acs_mode_var_decl(self):

        localctx = SwagLangParser.No_acs_mode_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_no_acs_mode_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(SwagLangParser.IDENT)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 278
                self.match(SwagLangParser.COLUMN)
                self.state = 279
                self.type_ann()


            self.state = 282
            self.match(SwagLangParser.ASSIGN)
            self.state = 283
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def L_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.L_BRACKET)
            else:
                return self.getToken(SwagLangParser.L_BRACKET, i)

        def R_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.R_BRACKET)
            else:
                return self.getToken(SwagLangParser.R_BRACKET, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.DOT)
            else:
                return self.getToken(SwagLangParser.DOT, i)

        def var_ref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Var_refContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Var_refContext,i)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.INT)
            else:
                return self.getToken(SwagLangParser.INT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.STRING)
            else:
                return self.getToken(SwagLangParser.STRING, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_var_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_ref" ):
                listener.enterVar_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_ref" ):
                listener.exitVar_ref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_ref" ):
                return visitor.visitVar_ref(self)
            else:
                return visitor.visitChildren(self)




    def var_ref(self):

        localctx = SwagLangParser.Var_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_ref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(SwagLangParser.IDENT)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 293
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [24]:
                        self.state = 286
                        self.match(SwagLangParser.L_BRACKET)
                        self.state = 288
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==52 or _la==53:
                            self.state = 287
                            _la = self._input.LA(1)
                            if not(_la==52 or _la==53):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()


                        self.state = 290
                        self.match(SwagLangParser.R_BRACKET)
                        pass
                    elif token in [28]:
                        self.state = 291
                        self.match(SwagLangParser.DOT)
                        self.state = 292
                        self.var_ref()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCESS_MOD(self):
            return self.getToken(SwagLangParser.ACCESS_MOD, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.IDENT)
            else:
                return self.getToken(SwagLangParser.IDENT, i)

        def ASSIGN(self):
            return self.getToken(SwagLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def type_ann(self):
            return self.getTypedRuleContext(SwagLangParser.Type_annContext,0)


        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = SwagLangParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 299
                self.match(SwagLangParser.IDENT)
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 300
                    self.match(SwagLangParser.COLUMN)
                    self.state = 301
                    self.type_ann()


                self.state = 304
                self.match(SwagLangParser.ASSIGN)
                self.state = 305
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 307
                self.match(SwagLangParser.IDENT)
                self.state = 310 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 308
                    self.match(SwagLangParser.COMMA)
                    self.state = 309
                    self.match(SwagLangParser.IDENT)
                    self.state = 312 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==27):
                        break

                self.state = 314
                self.match(SwagLangParser.ASSIGN)
                self.state = 315
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_ref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Var_refContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Var_refContext,i)


        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(SwagLangParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(SwagLangParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(SwagLangParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(SwagLangParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(SwagLangParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(SwagLangParser.MOD_ASSIGN, 0)

        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = SwagLangParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_assign)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.var_ref()
                self.state = 319
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 320
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.var_ref()
                self.state = 325 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 323
                    self.match(SwagLangParser.COMMA)
                    self.state = 324
                    self.var_ref()
                    self.state = 327 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==27):
                        break

                self.state = 329
                self.match(SwagLangParser.ASSIGN)
                self.state = 330
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(SwagLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_conditional_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_body" ):
                listener.enterConditional_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_body" ):
                listener.exitConditional_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_body" ):
                return visitor.visitConditional_body(self)
            else:
                return visitor.visitChildren(self)




    def conditional_body(self):

        localctx = SwagLangParser.Conditional_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_conditional_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(SwagLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_loop_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_body" ):
                listener.enterLoop_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_body" ):
                listener.exitLoop_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_body" ):
                return visitor.visitLoop_body(self)
            else:
                return visitor.visitChildren(self)




    def loop_body(self):

        localctx = SwagLangParser.Loop_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_loop(self):
            return self.getTypedRuleContext(SwagLangParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(SwagLangParser.While_loopContext,0)


        def do_while_loop(self):
            return self.getTypedRuleContext(SwagLangParser.Do_while_loopContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = SwagLangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_loop)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.for_loop()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.while_loop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 340
                self.do_while_loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SwagLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionContext,0)


        def loop_body(self):
            return self.getTypedRuleContext(SwagLangParser.Loop_bodyContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = SwagLangParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(SwagLangParser.WHILE)
            self.state = 344
            self.condition()
            self.state = 345
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(SwagLangParser.DO, 0)

        def loop_body(self):
            return self.getTypedRuleContext(SwagLangParser.Loop_bodyContext,0)


        def WHILE(self):
            return self.getToken(SwagLangParser.WHILE, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionContext,0)


        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_do_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_while_loop" ):
                listener.enterDo_while_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_while_loop" ):
                listener.exitDo_while_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_loop" ):
                return visitor.visitDo_while_loop(self)
            else:
                return visitor.visitChildren(self)




    def do_while_loop(self):

        localctx = SwagLangParser.Do_while_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_do_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(SwagLangParser.DO)
            self.state = 348
            self.loop_body()
            self.state = 349
            self.match(SwagLangParser.WHILE)
            self.state = 350
            self.match(SwagLangParser.L_PAREN)
            self.state = 351
            self.condition()
            self.state = 352
            self.match(SwagLangParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop_body(self):
            return self.getTypedRuleContext(SwagLangParser.Loop_bodyContext,0)


        def FOR(self):
            return self.getToken(SwagLangParser.FOR, 0)

        def forin(self):
            return self.getTypedRuleContext(SwagLangParser.ForinContext,0)


        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.SEMICOL)
            else:
                return self.getToken(SwagLangParser.SEMICOL, i)

        def no_acs_mode_var_decl(self):
            return self.getTypedRuleContext(SwagLangParser.No_acs_mode_var_declContext,0)


        def condition(self):
            return self.getTypedRuleContext(SwagLangParser.ConditionContext,0)


        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = SwagLangParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 354
                self.match(SwagLangParser.FOR)

                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 355
                    self.no_acs_mode_var_decl()


                self.state = 358
                self.match(SwagLangParser.SEMICOL)
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525334852763648) != 0):
                    self.state = 359
                    self.condition()


                self.state = 362
                self.match(SwagLangParser.SEMICOL)
                self.state = 364
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 363
                    self.expr(0)


                pass

            elif la_ == 2:
                self.state = 366
                self.forin()
                pass


            self.state = 369
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SwagLangParser.FOR, 0)

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def IN(self):
            return self.getToken(SwagLangParser.IN, 0)

        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def var_ref(self):
            return self.getTypedRuleContext(SwagLangParser.Var_refContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_forin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForin" ):
                listener.enterForin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForin" ):
                listener.exitForin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin" ):
                return visitor.visitForin(self)
            else:
                return visitor.visitChildren(self)




    def forin(self):

        localctx = SwagLangParser.ForinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(SwagLangParser.FOR)
            self.state = 372
            self.match(SwagLangParser.IDENT)
            self.state = 373
            self.match(SwagLangParser.IN)
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 374
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 375
                self.var_ref()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SwagLangParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ConditionContext,i)


        def conditional_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Conditional_bodyContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Conditional_bodyContext,i)


        def ELSE_IF(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.ELSE_IF)
            else:
                return self.getToken(SwagLangParser.ELSE_IF, i)

        def ELSE(self):
            return self.getToken(SwagLangParser.ELSE, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = SwagLangParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(SwagLangParser.IF)
            self.state = 379
            self.condition()
            self.state = 380
            self.conditional_body()
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 381
                self.match(SwagLangParser.ELSE_IF)
                self.state = 382
                self.condition()
                self.state = 383
                self.conditional_body()
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 390
                self.match(SwagLangParser.ELSE)
                self.state = 391
                self.conditional_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = SwagLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def data(self):
            return self.getTypedRuleContext(SwagLangParser.DataContext,0)


        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


        def var_ref(self):
            return self.getTypedRuleContext(SwagLangParser.Var_refContext,0)


        def INC(self):
            return self.getToken(SwagLangParser.INC, 0)

        def DEC(self):
            return self.getToken(SwagLangParser.DEC, 0)

        def NOT(self):
            return self.getToken(SwagLangParser.NOT, 0)

        def EXP(self):
            return self.getToken(SwagLangParser.EXP, 0)

        def MUL(self):
            return self.getToken(SwagLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(SwagLangParser.DIV, 0)

        def MOD(self):
            return self.getToken(SwagLangParser.MOD, 0)

        def PLUS(self):
            return self.getToken(SwagLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SwagLangParser.MINUS, 0)

        def GT(self):
            return self.getToken(SwagLangParser.GT, 0)

        def LT(self):
            return self.getToken(SwagLangParser.LT, 0)

        def EQ(self):
            return self.getToken(SwagLangParser.EQ, 0)

        def GTE(self):
            return self.getToken(SwagLangParser.GTE, 0)

        def LTE(self):
            return self.getToken(SwagLangParser.LTE, 0)

        def NEQ(self):
            return self.getToken(SwagLangParser.NEQ, 0)

        def AND(self):
            return self.getToken(SwagLangParser.AND, 0)

        def OR(self):
            return self.getToken(SwagLangParser.OR, 0)

        def QUESTION(self):
            return self.getToken(SwagLangParser.QUESTION, 0)

        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SwagLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 397
                self.match(SwagLangParser.L_PAREN)
                self.state = 398
                self.expr(0)
                self.state = 399
                self.match(SwagLangParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 401
                self.data()
                pass

            elif la_ == 3:
                self.state = 402
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 403
                self.var_ref()
                pass

            elif la_ == 5:
                self.state = 404
                self.var_ref()
                self.state = 405
                _la = self._input.LA(1)
                if not(_la==42 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.state = 407
                self.match(SwagLangParser.NOT)
                self.state = 408
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 435
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 411
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 412
                        self.match(SwagLangParser.EXP)
                        self.state = 413
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 414
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 415
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 416
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 417
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 418
                        _la = self._input.LA(1)
                        if not(_la==50 or _la==51):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 419
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 420
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 421
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1108307720798208) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 422
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 423
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 424
                        self.match(SwagLangParser.AND)
                        self.state = 425
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 426
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 427
                        self.match(SwagLangParser.OR)
                        self.state = 428
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 429
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 430
                        self.match(SwagLangParser.QUESTION)
                        self.state = 431
                        self.expr(0)
                        self.state = 432
                        self.match(SwagLangParser.COLUMN)
                        self.state = 433
                        self.expr(2)
                        pass

             
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def params(self):
            return self.getTypedRuleContext(SwagLangParser.ParamsContext,0)


        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = SwagLangParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(SwagLangParser.IDENT)
            self.state = 441
            self.match(SwagLangParser.L_PAREN)
            self.state = 442
            self.params()
            self.state = 443
            self.match(SwagLangParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def type_ann(self):
            return self.getTypedRuleContext(SwagLangParser.Type_annContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_param_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_decl" ):
                listener.enterParam_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_decl" ):
                listener.exitParam_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = SwagLangParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(SwagLangParser.IDENT)
            self.state = 446
            self.match(SwagLangParser.COLUMN)
            self.state = 447
            self.type_ann()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = SwagLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525334852763648) != 0):
                self.state = 449
                self.expr(0)
                self.state = 454
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 450
                        self.match(SwagLangParser.COMMA)
                        self.state = 451
                        self.expr(0) 
                    self.state = 456
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 457
                    self.match(SwagLangParser.COMMA)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




