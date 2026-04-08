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
        4,1,58,450,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,5,1,76,8,1,10,1,12,1,79,9,1,1,
        2,1,2,1,3,1,3,1,3,3,3,86,8,3,1,4,1,4,1,4,1,4,5,4,92,8,4,10,4,12,
        4,95,9,4,1,4,1,4,1,5,3,5,100,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,112,8,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,127,8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,135,8,10,
        10,10,12,10,138,9,10,1,10,3,10,141,8,10,3,10,143,8,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,156,8,11,1,12,
        1,12,1,12,5,12,161,8,12,10,12,12,12,164,9,12,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,172,8,13,10,13,12,13,175,9,13,3,13,177,8,13,1,13,
        1,13,5,13,181,8,13,10,13,12,13,184,9,13,1,13,1,13,4,13,188,8,13,
        11,13,12,13,189,1,13,5,13,193,8,13,10,13,12,13,196,9,13,1,13,5,13,
        199,8,13,10,13,12,13,202,9,13,3,13,204,8,13,1,13,1,13,1,14,1,14,
        3,14,210,8,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,
        221,8,15,1,16,1,16,1,16,1,16,5,16,227,8,16,10,16,12,16,230,9,16,
        1,16,3,16,233,8,16,3,16,235,8,16,1,16,1,16,1,17,1,17,5,17,241,8,
        17,10,17,12,17,244,9,17,1,17,1,17,1,17,5,17,249,8,17,10,17,12,17,
        252,9,17,1,17,5,17,255,8,17,10,17,12,17,258,9,17,1,17,3,17,261,8,
        17,3,17,263,8,17,1,17,5,17,266,8,17,10,17,12,17,269,9,17,1,17,1,
        17,1,18,1,18,1,18,3,18,276,8,18,1,18,1,18,1,18,1,19,1,19,1,19,3,
        19,284,8,19,1,19,1,19,1,19,5,19,289,8,19,10,19,12,19,292,9,19,1,
        20,1,20,1,20,1,20,3,20,298,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,3,20,308,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,3,21,320,8,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,3,24,329,
        8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,3,27,344,8,27,1,27,1,27,3,27,348,8,27,1,27,1,27,3,27,352,8,
        27,1,27,3,27,355,8,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,364,
        8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,5,29,373,8,29,10,29,12,29,
        376,9,29,1,29,1,29,3,29,380,8,29,1,30,1,30,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,397,8,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,423,8,31,10,
        31,12,31,426,9,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,
        34,1,34,1,34,5,34,440,8,34,10,34,12,34,443,9,34,1,34,3,34,446,8,
        34,3,34,448,8,34,1,34,0,1,62,35,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        0,7,2,0,4,4,17,17,1,0,52,53,1,0,29,34,1,0,42,43,1,0,39,41,1,0,50,
        51,1,0,44,49,490,0,70,1,0,0,0,2,77,1,0,0,0,4,80,1,0,0,0,6,85,1,0,
        0,0,8,87,1,0,0,0,10,99,1,0,0,0,12,111,1,0,0,0,14,113,1,0,0,0,16,
        116,1,0,0,0,18,126,1,0,0,0,20,128,1,0,0,0,22,155,1,0,0,0,24,157,
        1,0,0,0,26,165,1,0,0,0,28,207,1,0,0,0,30,220,1,0,0,0,32,222,1,0,
        0,0,34,238,1,0,0,0,36,272,1,0,0,0,38,280,1,0,0,0,40,307,1,0,0,0,
        42,319,1,0,0,0,44,321,1,0,0,0,46,323,1,0,0,0,48,328,1,0,0,0,50,330,
        1,0,0,0,52,334,1,0,0,0,54,354,1,0,0,0,56,358,1,0,0,0,58,365,1,0,
        0,0,60,381,1,0,0,0,62,396,1,0,0,0,64,427,1,0,0,0,66,432,1,0,0,0,
        68,447,1,0,0,0,70,71,3,2,1,0,71,72,5,0,0,1,72,1,1,0,0,0,73,76,3,
        4,2,0,74,76,5,55,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,
        75,1,0,0,0,77,78,1,0,0,0,78,3,1,0,0,0,79,77,1,0,0,0,80,81,3,6,3,
        0,81,5,1,0,0,0,82,86,3,20,10,0,83,86,3,40,20,0,84,86,3,26,13,0,85,
        82,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,7,1,0,0,0,87,93,5,22,0,
        0,88,89,3,10,5,0,89,90,5,55,0,0,90,92,1,0,0,0,91,88,1,0,0,0,92,95,
        1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,
        96,97,5,23,0,0,97,9,1,0,0,0,98,100,3,12,6,0,99,98,1,0,0,0,99,100,
        1,0,0,0,100,11,1,0,0,0,101,112,3,20,10,0,102,112,3,42,21,0,103,112,
        3,64,32,0,104,112,3,40,20,0,105,112,3,48,24,0,106,112,3,58,29,0,
        107,112,3,16,8,0,108,112,3,18,9,0,109,112,3,14,7,0,110,112,3,62,
        31,0,111,101,1,0,0,0,111,102,1,0,0,0,111,103,1,0,0,0,111,104,1,0,
        0,0,111,105,1,0,0,0,111,106,1,0,0,0,111,107,1,0,0,0,111,108,1,0,
        0,0,111,109,1,0,0,0,111,110,1,0,0,0,112,13,1,0,0,0,113,114,5,14,
        0,0,114,115,3,62,31,0,115,15,1,0,0,0,116,117,5,12,0,0,117,17,1,0,
        0,0,118,127,5,13,0,0,119,120,5,13,0,0,120,127,3,62,31,0,121,122,
        5,13,0,0,122,123,3,62,31,0,123,124,5,27,0,0,124,125,3,62,31,0,125,
        127,1,0,0,0,126,118,1,0,0,0,126,119,1,0,0,0,126,121,1,0,0,0,127,
        19,1,0,0,0,128,129,3,22,11,0,129,130,5,17,0,0,130,142,5,20,0,0,131,
        136,3,66,33,0,132,133,5,27,0,0,133,135,3,66,33,0,134,132,1,0,0,0,
        135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,140,1,0,0,0,
        138,136,1,0,0,0,139,141,5,27,0,0,140,139,1,0,0,0,140,141,1,0,0,0,
        141,143,1,0,0,0,142,131,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,
        144,145,5,21,0,0,145,146,3,8,4,0,146,21,1,0,0,0,147,156,3,24,12,
        0,148,156,5,3,0,0,149,150,5,20,0,0,150,151,5,17,0,0,151,152,5,27,
        0,0,152,153,3,24,12,0,153,154,5,21,0,0,154,156,1,0,0,0,155,147,1,
        0,0,0,155,148,1,0,0,0,155,149,1,0,0,0,156,23,1,0,0,0,157,162,7,0,
        0,0,158,159,5,24,0,0,159,161,5,25,0,0,160,158,1,0,0,0,161,164,1,
        0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,25,1,0,0,0,164,162,1,0,
        0,0,165,166,5,1,0,0,166,176,5,17,0,0,167,168,5,2,0,0,168,173,5,17,
        0,0,169,170,5,27,0,0,170,172,5,17,0,0,171,169,1,0,0,0,172,175,1,
        0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,177,1,0,0,0,175,173,1,
        0,0,0,176,167,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,182,5,
        22,0,0,179,181,5,55,0,0,180,179,1,0,0,0,181,184,1,0,0,0,182,180,
        1,0,0,0,182,183,1,0,0,0,183,203,1,0,0,0,184,182,1,0,0,0,185,194,
        3,28,14,0,186,188,5,55,0,0,187,186,1,0,0,0,188,189,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,191,193,3,28,14,0,192,187,
        1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,200,
        1,0,0,0,196,194,1,0,0,0,197,199,5,55,0,0,198,197,1,0,0,0,199,202,
        1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,204,1,0,0,0,202,200,
        1,0,0,0,203,185,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,
        5,23,0,0,206,27,1,0,0,0,207,209,5,17,0,0,208,210,5,26,0,0,209,208,
        1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,5,18,0,0,212,213,
        3,24,12,0,213,29,1,0,0,0,214,221,5,53,0,0,215,221,5,52,0,0,216,221,
        5,54,0,0,217,221,5,16,0,0,218,221,3,32,16,0,219,221,3,34,17,0,220,
        214,1,0,0,0,220,215,1,0,0,0,220,216,1,0,0,0,220,217,1,0,0,0,220,
        218,1,0,0,0,220,219,1,0,0,0,221,31,1,0,0,0,222,234,5,24,0,0,223,
        228,3,30,15,0,224,225,5,27,0,0,225,227,3,30,15,0,226,224,1,0,0,0,
        227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,232,1,0,0,0,
        230,228,1,0,0,0,231,233,5,27,0,0,232,231,1,0,0,0,232,233,1,0,0,0,
        233,235,1,0,0,0,234,223,1,0,0,0,234,235,1,0,0,0,235,236,1,0,0,0,
        236,237,5,25,0,0,237,33,1,0,0,0,238,242,5,22,0,0,239,241,5,55,0,
        0,240,239,1,0,0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,
        0,243,262,1,0,0,0,244,242,1,0,0,0,245,256,3,36,18,0,246,250,5,27,
        0,0,247,249,5,55,0,0,248,247,1,0,0,0,249,252,1,0,0,0,250,248,1,0,
        0,0,250,251,1,0,0,0,251,253,1,0,0,0,252,250,1,0,0,0,253,255,3,36,
        18,0,254,246,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,
        0,0,257,260,1,0,0,0,258,256,1,0,0,0,259,261,5,27,0,0,260,259,1,0,
        0,0,260,261,1,0,0,0,261,263,1,0,0,0,262,245,1,0,0,0,262,263,1,0,
        0,0,263,267,1,0,0,0,264,266,5,55,0,0,265,264,1,0,0,0,266,269,1,0,
        0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,267,1,0,
        0,0,270,271,5,23,0,0,271,35,1,0,0,0,272,275,5,17,0,0,273,274,5,18,
        0,0,274,276,3,24,12,0,275,273,1,0,0,0,275,276,1,0,0,0,276,277,1,
        0,0,0,277,278,5,29,0,0,278,279,3,62,31,0,279,37,1,0,0,0,280,290,
        5,17,0,0,281,283,5,24,0,0,282,284,7,1,0,0,283,282,1,0,0,0,283,284,
        1,0,0,0,284,285,1,0,0,0,285,289,5,25,0,0,286,287,5,28,0,0,287,289,
        3,38,19,0,288,281,1,0,0,0,288,286,1,0,0,0,289,292,1,0,0,0,290,288,
        1,0,0,0,290,291,1,0,0,0,291,39,1,0,0,0,292,290,1,0,0,0,293,294,5,
        15,0,0,294,297,5,17,0,0,295,296,5,18,0,0,296,298,3,24,12,0,297,295,
        1,0,0,0,297,298,1,0,0,0,298,299,1,0,0,0,299,300,5,29,0,0,300,308,
        3,62,31,0,301,302,5,15,0,0,302,303,5,17,0,0,303,304,5,27,0,0,304,
        305,5,17,0,0,305,306,5,29,0,0,306,308,3,64,32,0,307,293,1,0,0,0,
        307,301,1,0,0,0,308,41,1,0,0,0,309,310,3,38,19,0,310,311,7,2,0,0,
        311,312,3,62,31,0,312,320,1,0,0,0,313,314,3,38,19,0,314,315,5,27,
        0,0,315,316,3,38,19,0,316,317,5,29,0,0,317,318,3,64,32,0,318,320,
        1,0,0,0,319,309,1,0,0,0,319,313,1,0,0,0,320,43,1,0,0,0,321,322,3,
        8,4,0,322,45,1,0,0,0,323,324,3,8,4,0,324,47,1,0,0,0,325,329,3,54,
        27,0,326,329,3,50,25,0,327,329,3,52,26,0,328,325,1,0,0,0,328,326,
        1,0,0,0,328,327,1,0,0,0,329,49,1,0,0,0,330,331,5,10,0,0,331,332,
        3,60,30,0,332,333,3,46,23,0,333,51,1,0,0,0,334,335,5,11,0,0,335,
        336,3,46,23,0,336,337,5,10,0,0,337,338,5,20,0,0,338,339,3,60,30,
        0,339,340,5,21,0,0,340,53,1,0,0,0,341,343,5,8,0,0,342,344,3,36,18,
        0,343,342,1,0,0,0,343,344,1,0,0,0,344,345,1,0,0,0,345,347,5,19,0,
        0,346,348,3,60,30,0,347,346,1,0,0,0,347,348,1,0,0,0,348,349,1,0,
        0,0,349,351,5,19,0,0,350,352,3,62,31,0,351,350,1,0,0,0,351,352,1,
        0,0,0,352,355,1,0,0,0,353,355,3,56,28,0,354,341,1,0,0,0,354,353,
        1,0,0,0,355,356,1,0,0,0,356,357,3,46,23,0,357,55,1,0,0,0,358,359,
        5,8,0,0,359,360,5,17,0,0,360,363,5,9,0,0,361,364,3,64,32,0,362,364,
        3,38,19,0,363,361,1,0,0,0,363,362,1,0,0,0,364,57,1,0,0,0,365,366,
        5,5,0,0,366,367,3,60,30,0,367,374,3,44,22,0,368,369,5,6,0,0,369,
        370,3,60,30,0,370,371,3,44,22,0,371,373,1,0,0,0,372,368,1,0,0,0,
        373,376,1,0,0,0,374,372,1,0,0,0,374,375,1,0,0,0,375,379,1,0,0,0,
        376,374,1,0,0,0,377,378,5,7,0,0,378,380,3,44,22,0,379,377,1,0,0,
        0,379,380,1,0,0,0,380,59,1,0,0,0,381,382,3,62,31,0,382,61,1,0,0,
        0,383,384,6,31,-1,0,384,385,5,20,0,0,385,386,3,62,31,0,386,387,5,
        21,0,0,387,397,1,0,0,0,388,397,3,30,15,0,389,397,3,64,32,0,390,397,
        3,38,19,0,391,392,3,38,19,0,392,393,7,3,0,0,393,397,1,0,0,0,394,
        395,5,37,0,0,395,397,3,62,31,8,396,383,1,0,0,0,396,388,1,0,0,0,396,
        389,1,0,0,0,396,390,1,0,0,0,396,391,1,0,0,0,396,394,1,0,0,0,397,
        424,1,0,0,0,398,399,10,7,0,0,399,400,5,38,0,0,400,423,3,62,31,7,
        401,402,10,6,0,0,402,403,7,4,0,0,403,423,3,62,31,7,404,405,10,5,
        0,0,405,406,7,5,0,0,406,423,3,62,31,6,407,408,10,4,0,0,408,409,7,
        6,0,0,409,423,3,62,31,5,410,411,10,3,0,0,411,412,5,35,0,0,412,423,
        3,62,31,4,413,414,10,2,0,0,414,415,5,36,0,0,415,423,3,62,31,3,416,
        417,10,1,0,0,417,418,5,26,0,0,418,419,3,62,31,0,419,420,5,18,0,0,
        420,421,3,62,31,2,421,423,1,0,0,0,422,398,1,0,0,0,422,401,1,0,0,
        0,422,404,1,0,0,0,422,407,1,0,0,0,422,410,1,0,0,0,422,413,1,0,0,
        0,422,416,1,0,0,0,423,426,1,0,0,0,424,422,1,0,0,0,424,425,1,0,0,
        0,425,63,1,0,0,0,426,424,1,0,0,0,427,428,5,17,0,0,428,429,5,20,0,
        0,429,430,3,68,34,0,430,431,5,21,0,0,431,65,1,0,0,0,432,433,5,17,
        0,0,433,434,5,18,0,0,434,435,3,24,12,0,435,67,1,0,0,0,436,441,3,
        62,31,0,437,438,5,27,0,0,438,440,3,62,31,0,439,437,1,0,0,0,440,443,
        1,0,0,0,441,439,1,0,0,0,441,442,1,0,0,0,442,445,1,0,0,0,443,441,
        1,0,0,0,444,446,5,27,0,0,445,444,1,0,0,0,445,446,1,0,0,0,446,448,
        1,0,0,0,447,436,1,0,0,0,447,448,1,0,0,0,448,69,1,0,0,0,51,75,77,
        85,93,99,111,126,136,140,142,155,162,173,176,182,189,194,200,203,
        209,220,228,232,234,242,250,256,260,262,267,275,283,288,290,297,
        307,319,328,343,347,351,354,363,374,379,396,422,424,441,445,447
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


        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

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
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(SwagLangParser.RETURN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(SwagLangParser.RETURN)
                self.state = 120
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(SwagLangParser.RETURN)
                self.state = 122
                self.expr(0)
                self.state = 123
                self.match(SwagLangParser.COMMA)
                self.state = 124
                self.expr(0)
                pass


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
            self.state = 128
            self.return_type()
            self.state = 129
            self.match(SwagLangParser.IDENT)
            self.state = 130
            self.match(SwagLangParser.L_PAREN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 131
                self.param_decl()
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 132
                        self.match(SwagLangParser.COMMA)
                        self.state = 133
                        self.param_decl() 
                    self.state = 138
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 139
                    self.match(SwagLangParser.COMMA)




            self.state = 144
            self.match(SwagLangParser.R_PAREN)
            self.state = 145
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

        def type_ann(self):
            return self.getTypedRuleContext(SwagLangParser.Type_annContext,0)


        def VOID(self):
            return self.getToken(SwagLangParser.VOID, 0)

        def L_PAREN(self):
            return self.getToken(SwagLangParser.L_PAREN, 0)

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def R_PAREN(self):
            return self.getToken(SwagLangParser.R_PAREN, 0)

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
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.type_ann()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(SwagLangParser.VOID)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.match(SwagLangParser.L_PAREN)
                self.state = 150
                self.match(SwagLangParser.IDENT)
                self.state = 151
                self.match(SwagLangParser.COMMA)
                self.state = 152
                self.type_ann()
                self.state = 153
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
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==4 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 158
                self.match(SwagLangParser.L_BRACKET)
                self.state = 159
                self.match(SwagLangParser.R_BRACKET)
                self.state = 164
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
            self.state = 165
            self.match(SwagLangParser.INTERFACE)
            self.state = 166
            self.match(SwagLangParser.IDENT)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 167
                self.match(SwagLangParser.EXTENDS)
                self.state = 168
                self.match(SwagLangParser.IDENT)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 169
                    self.match(SwagLangParser.COMMA)
                    self.state = 170
                    self.match(SwagLangParser.IDENT)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 178
            self.match(SwagLangParser.L_CURLY)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 179
                self.match(SwagLangParser.NWLN)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 185
                self.interface_field()
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 187 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 186
                            self.match(SwagLangParser.NWLN)
                            self.state = 189 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==55):
                                break

                        self.state = 191
                        self.interface_field() 
                    self.state = 196
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 197
                    self.match(SwagLangParser.NWLN)
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 205
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
            self.state = 207
            self.match(SwagLangParser.IDENT)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 208
                self.match(SwagLangParser.QUESTION)


            self.state = 211
            self.match(SwagLangParser.COLUMN)
            self.state = 212
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
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(SwagLangParser.INT)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(SwagLangParser.STRING)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.match(SwagLangParser.FLOAT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.match(SwagLangParser.BOOL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 218
                self.list_()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 219
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
            self.state = 222
            self.match(SwagLangParser.L_BRACKET)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525197412630528) != 0):
                self.state = 223
                self.data()
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 224
                        self.match(SwagLangParser.COMMA)
                        self.state = 225
                        self.data() 
                    self.state = 230
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 231
                    self.match(SwagLangParser.COMMA)




            self.state = 236
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
            self.state = 238
            self.match(SwagLangParser.L_CURLY)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 239
                    self.match(SwagLangParser.NWLN) 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 245
                self.no_acs_mode_var_decl()
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 246
                        self.match(SwagLangParser.COMMA)
                        self.state = 250
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==55:
                            self.state = 247
                            self.match(SwagLangParser.NWLN)
                            self.state = 252
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 253
                        self.no_acs_mode_var_decl() 
                    self.state = 258
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 259
                    self.match(SwagLangParser.COMMA)




            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 264
                self.match(SwagLangParser.NWLN)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
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
            self.state = 272
            self.match(SwagLangParser.IDENT)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 273
                self.match(SwagLangParser.COLUMN)
                self.state = 274
                self.type_ann()


            self.state = 277
            self.match(SwagLangParser.ASSIGN)
            self.state = 278
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
            self.state = 280
            self.match(SwagLangParser.IDENT)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 288
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [24]:
                        self.state = 281
                        self.match(SwagLangParser.L_BRACKET)
                        self.state = 283
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==52 or _la==53:
                            self.state = 282
                            _la = self._input.LA(1)
                            if not(_la==52 or _la==53):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()


                        self.state = 285
                        self.match(SwagLangParser.R_BRACKET)
                        pass
                    elif token in [28]:
                        self.state = 286
                        self.match(SwagLangParser.DOT)
                        self.state = 287
                        self.var_ref()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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


        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


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
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 294
                self.match(SwagLangParser.IDENT)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 295
                    self.match(SwagLangParser.COLUMN)
                    self.state = 296
                    self.type_ann()


                self.state = 299
                self.match(SwagLangParser.ASSIGN)
                self.state = 300
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 302
                self.match(SwagLangParser.IDENT)
                self.state = 303
                self.match(SwagLangParser.COMMA)
                self.state = 304
                self.match(SwagLangParser.IDENT)
                self.state = 305
                self.match(SwagLangParser.ASSIGN)
                self.state = 306
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

        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def func_call(self):
            return self.getTypedRuleContext(SwagLangParser.Func_callContext,0)


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
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.var_ref()
                self.state = 310
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 311
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.var_ref()
                self.state = 314
                self.match(SwagLangParser.COMMA)
                self.state = 315
                self.var_ref()
                self.state = 316
                self.match(SwagLangParser.ASSIGN)
                self.state = 317
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
            self.state = 321
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
            self.state = 323
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
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.for_loop()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.while_loop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
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
            self.state = 330
            self.match(SwagLangParser.WHILE)
            self.state = 331
            self.condition()
            self.state = 332
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
            self.state = 334
            self.match(SwagLangParser.DO)
            self.state = 335
            self.loop_body()
            self.state = 336
            self.match(SwagLangParser.WHILE)
            self.state = 337
            self.match(SwagLangParser.L_PAREN)
            self.state = 338
            self.condition()
            self.state = 339
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
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 341
                self.match(SwagLangParser.FOR)

                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 342
                    self.no_acs_mode_var_decl()


                self.state = 345
                self.match(SwagLangParser.SEMICOL)
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525334852763648) != 0):
                    self.state = 346
                    self.condition()


                self.state = 349
                self.match(SwagLangParser.SEMICOL)
                self.state = 351
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 350
                    self.expr(0)


                pass

            elif la_ == 2:
                self.state = 353
                self.forin()
                pass


            self.state = 356
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
            self.state = 358
            self.match(SwagLangParser.FOR)
            self.state = 359
            self.match(SwagLangParser.IDENT)
            self.state = 360
            self.match(SwagLangParser.IN)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 361
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 362
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
            self.state = 365
            self.match(SwagLangParser.IF)
            self.state = 366
            self.condition()
            self.state = 367
            self.conditional_body()
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 368
                self.match(SwagLangParser.ELSE_IF)
                self.state = 369
                self.condition()
                self.state = 370
                self.conditional_body()
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 377
                self.match(SwagLangParser.ELSE)
                self.state = 378
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
            self.state = 381
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
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 384
                self.match(SwagLangParser.L_PAREN)
                self.state = 385
                self.expr(0)
                self.state = 386
                self.match(SwagLangParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 388
                self.data()
                pass

            elif la_ == 3:
                self.state = 389
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 390
                self.var_ref()
                pass

            elif la_ == 5:
                self.state = 391
                self.var_ref()
                self.state = 392
                _la = self._input.LA(1)
                if not(_la==42 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.state = 394
                self.match(SwagLangParser.NOT)
                self.state = 395
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 422
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 398
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 399
                        self.match(SwagLangParser.EXP)
                        self.state = 400
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 401
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 402
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 403
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 404
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 405
                        _la = self._input.LA(1)
                        if not(_la==50 or _la==51):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 406
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 407
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 408
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1108307720798208) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 409
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 410
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 411
                        self.match(SwagLangParser.AND)
                        self.state = 412
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 413
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 414
                        self.match(SwagLangParser.OR)
                        self.state = 415
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 416
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 417
                        self.match(SwagLangParser.QUESTION)
                        self.state = 418
                        self.expr(0)
                        self.state = 419
                        self.match(SwagLangParser.COLUMN)
                        self.state = 420
                        self.expr(2)
                        pass

             
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
            self.state = 427
            self.match(SwagLangParser.IDENT)
            self.state = 428
            self.match(SwagLangParser.L_PAREN)
            self.state = 429
            self.params()
            self.state = 430
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
            self.state = 432
            self.match(SwagLangParser.IDENT)
            self.state = 433
            self.match(SwagLangParser.COLUMN)
            self.state = 434
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
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31525334852763648) != 0):
                self.state = 436
                self.expr(0)
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 437
                        self.match(SwagLangParser.COMMA)
                        self.state = 438
                        self.expr(0) 
                    self.state = 443
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 444
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
         




