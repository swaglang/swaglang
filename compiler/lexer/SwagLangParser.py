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
        4,1,63,604,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,1,0,1,0,1,0,1,1,1,1,5,1,92,8,1,10,
        1,12,1,95,9,1,1,2,1,2,1,3,1,3,1,3,3,3,102,8,3,1,4,1,4,1,4,1,4,5,
        4,108,8,4,10,4,12,4,111,9,4,1,4,1,4,1,5,3,5,116,8,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,129,8,6,1,7,1,7,1,7,1,8,1,8,
        1,9,1,9,1,10,1,10,1,10,1,10,5,10,142,8,10,10,10,12,10,145,9,10,3,
        10,147,8,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,155,8,11,10,11,12,
        11,158,9,11,1,11,3,11,161,8,11,3,11,163,8,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,12,4,12,174,8,12,11,12,12,12,175,1,12,1,12,
        3,12,180,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,3,15,198,8,15,1,15,1,15,5,15,202,8,
        15,10,15,12,15,205,9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,213,8,
        16,10,16,12,16,216,9,16,3,16,218,8,16,1,16,1,16,5,16,222,8,16,10,
        16,12,16,225,9,16,1,16,1,16,4,16,229,8,16,11,16,12,16,230,1,16,5,
        16,234,8,16,10,16,12,16,237,9,16,1,16,5,16,240,8,16,10,16,12,16,
        243,9,16,3,16,245,8,16,1,16,1,16,1,17,1,17,3,17,251,8,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,266,
        8,18,1,19,1,19,5,19,270,8,19,10,19,12,19,273,9,19,1,19,1,19,1,19,
        5,19,278,8,19,10,19,12,19,281,9,19,1,19,5,19,284,8,19,10,19,12,19,
        287,9,19,1,19,3,19,290,8,19,3,19,292,8,19,1,19,5,19,295,8,19,10,
        19,12,19,298,9,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,
        21,5,21,310,8,21,10,21,12,21,313,9,21,1,21,1,21,1,21,5,21,318,8,
        21,10,21,12,21,321,9,21,1,21,5,21,324,8,21,10,21,12,21,327,9,21,
        1,21,3,21,330,8,21,3,21,332,8,21,1,21,5,21,335,8,21,10,21,12,21,
        338,9,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,5,23,349,8,
        23,10,23,12,23,352,9,23,1,23,1,23,1,23,5,23,357,8,23,10,23,12,23,
        360,9,23,1,23,5,23,363,8,23,10,23,12,23,366,9,23,1,23,3,23,369,8,
        23,3,23,371,8,23,1,23,5,23,374,8,23,10,23,12,23,377,9,23,1,23,1,
        23,1,24,1,24,5,24,383,8,24,10,24,12,24,386,9,24,1,24,1,24,1,24,5,
        24,391,8,24,10,24,12,24,394,9,24,1,24,5,24,397,8,24,10,24,12,24,
        400,9,24,1,24,3,24,403,8,24,3,24,405,8,24,1,24,5,24,408,8,24,10,
        24,12,24,411,9,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,3,
        26,422,8,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,5,
        27,434,8,27,10,27,12,27,437,9,27,1,28,1,28,1,28,1,28,3,28,443,8,
        28,1,28,1,28,1,28,1,28,1,28,1,28,4,28,451,8,28,11,28,12,28,452,1,
        28,1,28,3,28,457,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,4,29,466,
        8,29,11,29,12,29,467,1,29,1,29,1,29,3,29,473,8,29,1,30,1,30,1,31,
        1,31,1,32,1,32,1,32,3,32,482,8,32,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,35,1,35,3,35,497,8,35,1,35,1,35,3,35,
        501,8,35,1,35,1,35,1,35,3,35,506,8,35,1,35,3,35,509,8,35,1,35,1,
        35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,5,
        37,525,8,37,10,37,12,37,528,9,37,1,37,1,37,3,37,532,8,37,1,38,1,
        38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,
        39,1,39,1,39,3,39,551,8,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,
        39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,
        39,1,39,1,39,1,39,5,39,577,8,39,10,39,12,39,580,9,39,1,40,1,40,1,
        40,1,40,1,40,1,41,1,41,1,41,1,41,1,42,1,42,1,42,5,42,594,8,42,10,
        42,12,42,597,9,42,1,42,3,42,600,8,42,3,42,602,8,42,1,42,0,1,78,43,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,0,5,
        1,0,34,39,1,0,47,48,1,0,44,46,1,0,55,56,1,0,49,54,662,0,86,1,0,0,
        0,2,93,1,0,0,0,4,96,1,0,0,0,6,101,1,0,0,0,8,103,1,0,0,0,10,115,1,
        0,0,0,12,128,1,0,0,0,14,130,1,0,0,0,16,133,1,0,0,0,18,135,1,0,0,
        0,20,137,1,0,0,0,22,148,1,0,0,0,24,179,1,0,0,0,26,181,1,0,0,0,28,
        188,1,0,0,0,30,197,1,0,0,0,32,206,1,0,0,0,34,248,1,0,0,0,36,265,
        1,0,0,0,38,267,1,0,0,0,40,301,1,0,0,0,42,306,1,0,0,0,44,342,1,0,
        0,0,46,346,1,0,0,0,48,380,1,0,0,0,50,414,1,0,0,0,52,418,1,0,0,0,
        54,426,1,0,0,0,56,456,1,0,0,0,58,472,1,0,0,0,60,474,1,0,0,0,62,476,
        1,0,0,0,64,481,1,0,0,0,66,483,1,0,0,0,68,487,1,0,0,0,70,508,1,0,
        0,0,72,512,1,0,0,0,74,517,1,0,0,0,76,533,1,0,0,0,78,550,1,0,0,0,
        80,581,1,0,0,0,82,586,1,0,0,0,84,601,1,0,0,0,86,87,3,2,1,0,87,88,
        5,0,0,1,88,1,1,0,0,0,89,92,3,4,2,0,90,92,5,60,0,0,91,89,1,0,0,0,
        91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,3,1,0,
        0,0,95,93,1,0,0,0,96,97,3,6,3,0,97,5,1,0,0,0,98,102,3,22,11,0,99,
        102,3,56,28,0,100,102,3,32,16,0,101,98,1,0,0,0,101,99,1,0,0,0,101,
        100,1,0,0,0,102,7,1,0,0,0,103,109,5,26,0,0,104,105,3,10,5,0,105,
        106,5,60,0,0,106,108,1,0,0,0,107,104,1,0,0,0,108,111,1,0,0,0,109,
        107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,0,0,0,112,
        113,5,27,0,0,113,9,1,0,0,0,114,116,3,12,6,0,115,114,1,0,0,0,115,
        116,1,0,0,0,116,11,1,0,0,0,117,129,3,22,11,0,118,129,3,58,29,0,119,
        129,3,80,40,0,120,129,3,56,28,0,121,129,3,64,32,0,122,129,3,74,37,
        0,123,129,3,16,8,0,124,129,3,18,9,0,125,129,3,20,10,0,126,129,3,
        14,7,0,127,129,3,78,39,0,128,117,1,0,0,0,128,118,1,0,0,0,128,119,
        1,0,0,0,128,120,1,0,0,0,128,121,1,0,0,0,128,122,1,0,0,0,128,123,
        1,0,0,0,128,124,1,0,0,0,128,125,1,0,0,0,128,126,1,0,0,0,128,127,
        1,0,0,0,129,13,1,0,0,0,130,131,5,17,0,0,131,132,3,78,39,0,132,15,
        1,0,0,0,133,134,5,14,0,0,134,17,1,0,0,0,135,136,5,15,0,0,136,19,
        1,0,0,0,137,146,5,16,0,0,138,143,3,78,39,0,139,140,5,31,0,0,140,
        142,3,78,39,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,
        144,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,146,138,1,0,0,0,146,
        147,1,0,0,0,147,21,1,0,0,0,148,149,3,24,12,0,149,150,5,21,0,0,150,
        162,5,24,0,0,151,156,3,82,41,0,152,153,5,31,0,0,153,155,3,82,41,
        0,154,152,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,
        0,157,160,1,0,0,0,158,156,1,0,0,0,159,161,5,31,0,0,160,159,1,0,0,
        0,160,161,1,0,0,0,161,163,1,0,0,0,162,151,1,0,0,0,162,163,1,0,0,
        0,163,164,1,0,0,0,164,165,5,25,0,0,165,166,3,8,4,0,166,23,1,0,0,
        0,167,180,3,30,15,0,168,180,5,3,0,0,169,170,5,24,0,0,170,173,3,30,
        15,0,171,172,5,31,0,0,172,174,3,30,15,0,173,171,1,0,0,0,174,175,
        1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,
        5,25,0,0,178,180,1,0,0,0,179,167,1,0,0,0,179,168,1,0,0,0,179,169,
        1,0,0,0,180,25,1,0,0,0,181,182,5,4,0,0,182,183,5,50,0,0,183,184,
        3,30,15,0,184,185,5,31,0,0,185,186,3,30,15,0,186,187,5,49,0,0,187,
        27,1,0,0,0,188,189,5,5,0,0,189,190,5,50,0,0,190,191,3,30,15,0,191,
        192,5,49,0,0,192,29,1,0,0,0,193,198,5,6,0,0,194,198,3,26,13,0,195,
        198,3,28,14,0,196,198,5,21,0,0,197,193,1,0,0,0,197,194,1,0,0,0,197,
        195,1,0,0,0,197,196,1,0,0,0,198,203,1,0,0,0,199,200,5,28,0,0,200,
        202,5,29,0,0,201,199,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,
        204,1,0,0,0,204,31,1,0,0,0,205,203,1,0,0,0,206,207,5,1,0,0,207,217,
        5,21,0,0,208,209,5,2,0,0,209,214,5,21,0,0,210,211,5,31,0,0,211,213,
        5,21,0,0,212,210,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,
        1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,217,208,1,0,0,0,217,218,
        1,0,0,0,218,219,1,0,0,0,219,223,5,26,0,0,220,222,5,60,0,0,221,220,
        1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,244,
        1,0,0,0,225,223,1,0,0,0,226,235,3,34,17,0,227,229,5,60,0,0,228,227,
        1,0,0,0,229,230,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,232,
        1,0,0,0,232,234,3,34,17,0,233,228,1,0,0,0,234,237,1,0,0,0,235,233,
        1,0,0,0,235,236,1,0,0,0,236,241,1,0,0,0,237,235,1,0,0,0,238,240,
        5,60,0,0,239,238,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,
        1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,244,226,1,0,0,0,244,245,
        1,0,0,0,245,246,1,0,0,0,246,247,5,27,0,0,247,33,1,0,0,0,248,250,
        5,21,0,0,249,251,5,30,0,0,250,249,1,0,0,0,250,251,1,0,0,0,251,252,
        1,0,0,0,252,253,5,22,0,0,253,254,3,30,15,0,254,35,1,0,0,0,255,266,
        5,58,0,0,256,266,5,57,0,0,257,266,5,59,0,0,258,266,5,19,0,0,259,
        266,5,20,0,0,260,266,3,38,19,0,261,266,3,40,20,0,262,266,3,42,21,
        0,263,266,3,46,23,0,264,266,3,48,24,0,265,255,1,0,0,0,265,256,1,
        0,0,0,265,257,1,0,0,0,265,258,1,0,0,0,265,259,1,0,0,0,265,260,1,
        0,0,0,265,261,1,0,0,0,265,262,1,0,0,0,265,263,1,0,0,0,265,264,1,
        0,0,0,266,37,1,0,0,0,267,271,5,28,0,0,268,270,5,60,0,0,269,268,1,
        0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,291,1,
        0,0,0,273,271,1,0,0,0,274,285,3,78,39,0,275,279,5,31,0,0,276,278,
        5,60,0,0,277,276,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,
        1,0,0,0,280,282,1,0,0,0,281,279,1,0,0,0,282,284,3,78,39,0,283,275,
        1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,289,
        1,0,0,0,287,285,1,0,0,0,288,290,5,31,0,0,289,288,1,0,0,0,289,290,
        1,0,0,0,290,292,1,0,0,0,291,274,1,0,0,0,291,292,1,0,0,0,292,296,
        1,0,0,0,293,295,5,60,0,0,294,293,1,0,0,0,295,298,1,0,0,0,296,294,
        1,0,0,0,296,297,1,0,0,0,297,299,1,0,0,0,298,296,1,0,0,0,299,300,
        5,29,0,0,300,39,1,0,0,0,301,302,5,6,0,0,302,303,5,28,0,0,303,304,
        3,78,39,0,304,305,5,29,0,0,305,41,1,0,0,0,306,307,5,26,0,0,307,311,
        5,26,0,0,308,310,5,60,0,0,309,308,1,0,0,0,310,313,1,0,0,0,311,309,
        1,0,0,0,311,312,1,0,0,0,312,331,1,0,0,0,313,311,1,0,0,0,314,325,
        3,44,22,0,315,319,5,31,0,0,316,318,5,60,0,0,317,316,1,0,0,0,318,
        321,1,0,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,322,1,0,0,0,321,
        319,1,0,0,0,322,324,3,44,22,0,323,315,1,0,0,0,324,327,1,0,0,0,325,
        323,1,0,0,0,325,326,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,328,
        330,5,31,0,0,329,328,1,0,0,0,329,330,1,0,0,0,330,332,1,0,0,0,331,
        314,1,0,0,0,331,332,1,0,0,0,332,336,1,0,0,0,333,335,5,60,0,0,334,
        333,1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,337,1,0,0,0,337,
        339,1,0,0,0,338,336,1,0,0,0,339,340,5,27,0,0,340,341,5,27,0,0,341,
        43,1,0,0,0,342,343,3,78,39,0,343,344,5,22,0,0,344,345,3,78,39,0,
        345,45,1,0,0,0,346,350,5,33,0,0,347,349,5,60,0,0,348,347,1,0,0,0,
        349,352,1,0,0,0,350,348,1,0,0,0,350,351,1,0,0,0,351,370,1,0,0,0,
        352,350,1,0,0,0,353,364,3,78,39,0,354,358,5,31,0,0,355,357,5,60,
        0,0,356,355,1,0,0,0,357,360,1,0,0,0,358,356,1,0,0,0,358,359,1,0,
        0,0,359,361,1,0,0,0,360,358,1,0,0,0,361,363,3,78,39,0,362,354,1,
        0,0,0,363,366,1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,368,1,
        0,0,0,366,364,1,0,0,0,367,369,5,31,0,0,368,367,1,0,0,0,368,369,1,
        0,0,0,369,371,1,0,0,0,370,353,1,0,0,0,370,371,1,0,0,0,371,375,1,
        0,0,0,372,374,5,60,0,0,373,372,1,0,0,0,374,377,1,0,0,0,375,373,1,
        0,0,0,375,376,1,0,0,0,376,378,1,0,0,0,377,375,1,0,0,0,378,379,5,
        29,0,0,379,47,1,0,0,0,380,384,5,26,0,0,381,383,5,60,0,0,382,381,
        1,0,0,0,383,386,1,0,0,0,384,382,1,0,0,0,384,385,1,0,0,0,385,404,
        1,0,0,0,386,384,1,0,0,0,387,398,3,50,25,0,388,392,5,31,0,0,389,391,
        5,60,0,0,390,389,1,0,0,0,391,394,1,0,0,0,392,390,1,0,0,0,392,393,
        1,0,0,0,393,395,1,0,0,0,394,392,1,0,0,0,395,397,3,50,25,0,396,388,
        1,0,0,0,397,400,1,0,0,0,398,396,1,0,0,0,398,399,1,0,0,0,399,402,
        1,0,0,0,400,398,1,0,0,0,401,403,5,31,0,0,402,401,1,0,0,0,402,403,
        1,0,0,0,403,405,1,0,0,0,404,387,1,0,0,0,404,405,1,0,0,0,405,409,
        1,0,0,0,406,408,5,60,0,0,407,406,1,0,0,0,408,411,1,0,0,0,409,407,
        1,0,0,0,409,410,1,0,0,0,410,412,1,0,0,0,411,409,1,0,0,0,412,413,
        5,27,0,0,413,49,1,0,0,0,414,415,5,21,0,0,415,416,5,22,0,0,416,417,
        3,78,39,0,417,51,1,0,0,0,418,421,5,21,0,0,419,420,5,22,0,0,420,422,
        3,30,15,0,421,419,1,0,0,0,421,422,1,0,0,0,422,423,1,0,0,0,423,424,
        5,34,0,0,424,425,3,78,39,0,425,53,1,0,0,0,426,435,5,21,0,0,427,428,
        5,28,0,0,428,429,3,78,39,0,429,430,5,29,0,0,430,434,1,0,0,0,431,
        432,5,32,0,0,432,434,3,54,27,0,433,427,1,0,0,0,433,431,1,0,0,0,434,
        437,1,0,0,0,435,433,1,0,0,0,435,436,1,0,0,0,436,55,1,0,0,0,437,435,
        1,0,0,0,438,439,5,18,0,0,439,442,5,21,0,0,440,441,5,22,0,0,441,443,
        3,30,15,0,442,440,1,0,0,0,442,443,1,0,0,0,443,444,1,0,0,0,444,445,
        5,34,0,0,445,457,3,78,39,0,446,447,5,18,0,0,447,450,5,21,0,0,448,
        449,5,31,0,0,449,451,5,21,0,0,450,448,1,0,0,0,451,452,1,0,0,0,452,
        450,1,0,0,0,452,453,1,0,0,0,453,454,1,0,0,0,454,455,5,34,0,0,455,
        457,3,80,40,0,456,438,1,0,0,0,456,446,1,0,0,0,457,57,1,0,0,0,458,
        459,3,54,27,0,459,460,7,0,0,0,460,461,3,78,39,0,461,473,1,0,0,0,
        462,465,3,54,27,0,463,464,5,31,0,0,464,466,3,54,27,0,465,463,1,0,
        0,0,466,467,1,0,0,0,467,465,1,0,0,0,467,468,1,0,0,0,468,469,1,0,
        0,0,469,470,5,34,0,0,470,471,3,80,40,0,471,473,1,0,0,0,472,458,1,
        0,0,0,472,462,1,0,0,0,473,59,1,0,0,0,474,475,3,8,4,0,475,61,1,0,
        0,0,476,477,3,8,4,0,477,63,1,0,0,0,478,482,3,70,35,0,479,482,3,66,
        33,0,480,482,3,68,34,0,481,478,1,0,0,0,481,479,1,0,0,0,481,480,1,
        0,0,0,482,65,1,0,0,0,483,484,5,12,0,0,484,485,3,76,38,0,485,486,
        3,62,31,0,486,67,1,0,0,0,487,488,5,13,0,0,488,489,3,62,31,0,489,
        490,5,12,0,0,490,491,5,24,0,0,491,492,3,76,38,0,492,493,5,25,0,0,
        493,69,1,0,0,0,494,496,5,10,0,0,495,497,3,52,26,0,496,495,1,0,0,
        0,496,497,1,0,0,0,497,498,1,0,0,0,498,500,5,23,0,0,499,501,3,76,
        38,0,500,499,1,0,0,0,500,501,1,0,0,0,501,502,1,0,0,0,502,505,5,23,
        0,0,503,506,3,58,29,0,504,506,3,78,39,0,505,503,1,0,0,0,505,504,
        1,0,0,0,505,506,1,0,0,0,506,509,1,0,0,0,507,509,3,72,36,0,508,494,
        1,0,0,0,508,507,1,0,0,0,509,510,1,0,0,0,510,511,3,62,31,0,511,71,
        1,0,0,0,512,513,5,10,0,0,513,514,5,21,0,0,514,515,5,11,0,0,515,516,
        3,78,39,0,516,73,1,0,0,0,517,518,5,7,0,0,518,519,3,76,38,0,519,526,
        3,60,30,0,520,521,5,8,0,0,521,522,3,76,38,0,522,523,3,60,30,0,523,
        525,1,0,0,0,524,520,1,0,0,0,525,528,1,0,0,0,526,524,1,0,0,0,526,
        527,1,0,0,0,527,531,1,0,0,0,528,526,1,0,0,0,529,530,5,9,0,0,530,
        532,3,60,30,0,531,529,1,0,0,0,531,532,1,0,0,0,532,75,1,0,0,0,533,
        534,3,78,39,0,534,77,1,0,0,0,535,536,6,39,-1,0,536,537,5,24,0,0,
        537,538,3,78,39,0,538,539,5,25,0,0,539,551,1,0,0,0,540,551,3,36,
        18,0,541,551,3,80,40,0,542,551,3,54,27,0,543,544,3,54,27,0,544,545,
        7,1,0,0,545,551,1,0,0,0,546,547,5,42,0,0,547,551,3,78,39,9,548,549,
        5,56,0,0,549,551,3,78,39,8,550,535,1,0,0,0,550,540,1,0,0,0,550,541,
        1,0,0,0,550,542,1,0,0,0,550,543,1,0,0,0,550,546,1,0,0,0,550,548,
        1,0,0,0,551,578,1,0,0,0,552,553,10,7,0,0,553,554,5,43,0,0,554,577,
        3,78,39,7,555,556,10,6,0,0,556,557,7,2,0,0,557,577,3,78,39,7,558,
        559,10,5,0,0,559,560,7,3,0,0,560,577,3,78,39,6,561,562,10,4,0,0,
        562,563,7,4,0,0,563,577,3,78,39,5,564,565,10,3,0,0,565,566,5,40,
        0,0,566,577,3,78,39,4,567,568,10,2,0,0,568,569,5,41,0,0,569,577,
        3,78,39,3,570,571,10,1,0,0,571,572,5,30,0,0,572,573,3,78,39,0,573,
        574,5,22,0,0,574,575,3,78,39,2,575,577,1,0,0,0,576,552,1,0,0,0,576,
        555,1,0,0,0,576,558,1,0,0,0,576,561,1,0,0,0,576,564,1,0,0,0,576,
        567,1,0,0,0,576,570,1,0,0,0,577,580,1,0,0,0,578,576,1,0,0,0,578,
        579,1,0,0,0,579,79,1,0,0,0,580,578,1,0,0,0,581,582,5,21,0,0,582,
        583,5,24,0,0,583,584,3,84,42,0,584,585,5,25,0,0,585,81,1,0,0,0,586,
        587,5,21,0,0,587,588,5,22,0,0,588,589,3,30,15,0,589,83,1,0,0,0,590,
        595,3,78,39,0,591,592,5,31,0,0,592,594,3,78,39,0,593,591,1,0,0,0,
        594,597,1,0,0,0,595,593,1,0,0,0,595,596,1,0,0,0,596,599,1,0,0,0,
        597,595,1,0,0,0,598,600,5,31,0,0,599,598,1,0,0,0,599,600,1,0,0,0,
        600,602,1,0,0,0,601,590,1,0,0,0,601,602,1,0,0,0,602,85,1,0,0,0,69,
        91,93,101,109,115,128,143,146,156,160,162,175,179,197,203,214,217,
        223,230,235,241,244,250,265,271,279,285,289,291,296,311,319,325,
        329,331,336,350,358,364,368,370,375,384,392,398,402,404,409,421,
        433,435,442,452,456,467,472,481,496,500,505,508,526,531,550,576,
        578,595,599,601
    ]

class SwagLangParser ( Parser ):

    grammarFileName = "SwagLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'interface'", "'extends'", "'void'", 
                     "'map'", "'set'", "<INVALID>", "'if'", "<INVALID>", 
                     "'else'", "'for'", "'in'", "'while'", "'do'", "'break'", 
                     "'continue'", "'return'", "'defer'", "<INVALID>", "<INVALID>", 
                     "'null'", "<INVALID>", "':'", "';'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "'?'", "','", "'.'", "'#['", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'&&'", 
                     "'||'", "'!'", "'**'", "'*'", "'/'", "'%'", "'++'", 
                     "'--'", "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INTERFACE", "EXTENDS", "VOID", "MAP", 
                      "SET", "TYPE", "IF", "ELSE_IF", "ELSE", "FOR", "IN", 
                      "WHILE", "DO", "BREAK", "CONTINUE", "RETURN", "DEFER", 
                      "ACCESS_MOD", "BOOL", "NULL", "IDENT", "COLUMN", "SEMICOL", 
                      "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", 
                      "R_BRACKET", "QUESTION", "COMMA", "DOT", "SET_START", 
                      "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "AND", "OR", "NOT", "EXP", 
                      "MUL", "DIV", "MOD", "INC", "DEC", "GT", "LT", "EQ", 
                      "NEQ", "GTE", "LTE", "PLUS", "MINUS", "STRING", "INT", 
                      "FLOAT", "NWLN", "SPACE", "COMMENT", "INLINE_COMMENT" ]

    RULE_prog = 0
    RULE_stmts = 1
    RULE_stmt = 2
    RULE_pure_stmt = 3
    RULE_code_block = 4
    RULE_func_stmt = 5
    RULE_pure_func_stmt = 6
    RULE_defer = 7
    RULE_break = 8
    RULE_continue = 9
    RULE_return = 10
    RULE_func_decl = 11
    RULE_return_type = 12
    RULE_map_type = 13
    RULE_set_type = 14
    RULE_type_ann = 15
    RULE_interface_decl = 16
    RULE_interface_field = 17
    RULE_data = 18
    RULE_array = 19
    RULE_array_alloc = 20
    RULE_map = 21
    RULE_map_field = 22
    RULE_set = 23
    RULE_struct = 24
    RULE_struct_field = 25
    RULE_no_acs_mode_var_decl = 26
    RULE_var_ref = 27
    RULE_var_decl = 28
    RULE_var_assign = 29
    RULE_conditional_body = 30
    RULE_loop_body = 31
    RULE_loop = 32
    RULE_while_loop = 33
    RULE_do_while_loop = 34
    RULE_for_loop = 35
    RULE_forin = 36
    RULE_conditional = 37
    RULE_condition = 38
    RULE_expr = 39
    RULE_func_call = 40
    RULE_param_decl = 41
    RULE_params = 42

    ruleNames =  [ "prog", "stmts", "stmt", "pure_stmt", "code_block", "func_stmt", 
                   "pure_func_stmt", "defer", "break", "continue", "return", 
                   "func_decl", "return_type", "map_type", "set_type", "type_ann", 
                   "interface_decl", "interface_field", "data", "array", 
                   "array_alloc", "map", "map_field", "set", "struct", "struct_field", 
                   "no_acs_mode_var_decl", "var_ref", "var_decl", "var_assign", 
                   "conditional_body", "loop_body", "loop", "while_loop", 
                   "do_while_loop", "for_loop", "forin", "conditional", 
                   "condition", "expr", "func_call", "param_decl", "params" ]

    EOF = Token.EOF
    INTERFACE=1
    EXTENDS=2
    VOID=3
    MAP=4
    SET=5
    TYPE=6
    IF=7
    ELSE_IF=8
    ELSE=9
    FOR=10
    IN=11
    WHILE=12
    DO=13
    BREAK=14
    CONTINUE=15
    RETURN=16
    DEFER=17
    ACCESS_MOD=18
    BOOL=19
    NULL=20
    IDENT=21
    COLUMN=22
    SEMICOL=23
    L_PAREN=24
    R_PAREN=25
    L_CURLY=26
    R_CURLY=27
    L_BRACKET=28
    R_BRACKET=29
    QUESTION=30
    COMMA=31
    DOT=32
    SET_START=33
    ASSIGN=34
    ADD_ASSIGN=35
    SUB_ASSIGN=36
    MUL_ASSIGN=37
    DIV_ASSIGN=38
    MOD_ASSIGN=39
    AND=40
    OR=41
    NOT=42
    EXP=43
    MUL=44
    DIV=45
    MOD=46
    INC=47
    DEC=48
    GT=49
    LT=50
    EQ=51
    NEQ=52
    GTE=53
    LTE=54
    PLUS=55
    MINUS=56
    STRING=57
    INT=58
    FLOAT=59
    NWLN=60
    SPACE=61
    COMMENT=62
    INLINE_COMMENT=63

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
            self.state = 86
            self.stmts()
            self.state = 87
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
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921504625983610) != 0):
                self.state = 91
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 4, 5, 6, 18, 21, 24]:
                    self.state = 89
                    self.stmt()
                    pass
                elif token in [60]:
                    self.state = 90
                    self.match(SwagLangParser.NWLN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 95
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
            self.state = 96
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
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 21, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.func_decl()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.var_decl()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
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
            self.state = 103
            self.match(SwagLangParser.L_CURLY)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2233789822168724728) != 0):
                self.state = 104
                self.func_stmt()
                self.state = 105
                self.match(SwagLangParser.NWLN)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
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
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080868317561877752) != 0):
                self.state = 114
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


        def continue_(self):
            return self.getTypedRuleContext(SwagLangParser.ContinueContext,0)


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
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.var_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.var_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 122
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.break_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 124
                self.continue_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 125
                self.return_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 126
                self.defer()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 127
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
            self.state = 130
            self.match(SwagLangParser.DEFER)
            self.state = 131
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
            self.state = 133
            self.match(SwagLangParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(SwagLangParser.CONTINUE, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_continue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue" ):
                listener.enterContinue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue" ):
                listener.exitContinue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)




    def continue_(self):

        localctx = SwagLangParser.ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(SwagLangParser.CONTINUE)
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
        self.enterRule(localctx, 20, self.RULE_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(SwagLangParser.RETURN)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080868317561356352) != 0):
                self.state = 138
                self.expr(0)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 139
                    self.match(SwagLangParser.COMMA)
                    self.state = 140
                    self.expr(0)
                    self.state = 145
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
        self.enterRule(localctx, 22, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.return_type()
            self.state = 149
            self.match(SwagLangParser.IDENT)
            self.state = 150
            self.match(SwagLangParser.L_PAREN)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 151
                self.param_decl()
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 152
                        self.match(SwagLangParser.COMMA)
                        self.state = 153
                        self.param_decl() 
                    self.state = 158
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 159
                    self.match(SwagLangParser.COMMA)




            self.state = 164
            self.match(SwagLangParser.R_PAREN)
            self.state = 165
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
        self.enterRule(localctx, 24, self.RULE_return_type)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.type_ann()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(SwagLangParser.VOID)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.match(SwagLangParser.L_PAREN)
                self.state = 170
                self.type_ann()
                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 171
                    self.match(SwagLangParser.COMMA)
                    self.state = 172
                    self.type_ann()
                    self.state = 175 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                self.state = 177
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


    class Map_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(SwagLangParser.MAP, 0)

        def LT(self):
            return self.getToken(SwagLangParser.LT, 0)

        def type_ann(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Type_annContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Type_annContext,i)


        def COMMA(self):
            return self.getToken(SwagLangParser.COMMA, 0)

        def GT(self):
            return self.getToken(SwagLangParser.GT, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_map_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_type" ):
                listener.enterMap_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_type" ):
                listener.exitMap_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_type" ):
                return visitor.visitMap_type(self)
            else:
                return visitor.visitChildren(self)




    def map_type(self):

        localctx = SwagLangParser.Map_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(SwagLangParser.MAP)
            self.state = 182
            self.match(SwagLangParser.LT)
            self.state = 183
            self.type_ann()
            self.state = 184
            self.match(SwagLangParser.COMMA)
            self.state = 185
            self.type_ann()
            self.state = 186
            self.match(SwagLangParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(SwagLangParser.SET, 0)

        def LT(self):
            return self.getToken(SwagLangParser.LT, 0)

        def type_ann(self):
            return self.getTypedRuleContext(SwagLangParser.Type_annContext,0)


        def GT(self):
            return self.getToken(SwagLangParser.GT, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_set_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_type" ):
                listener.enterSet_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_type" ):
                listener.exitSet_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_type" ):
                return visitor.visitSet_type(self)
            else:
                return visitor.visitChildren(self)




    def set_type(self):

        localctx = SwagLangParser.Set_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_set_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(SwagLangParser.SET)
            self.state = 189
            self.match(SwagLangParser.LT)
            self.state = 190
            self.type_ann()
            self.state = 191
            self.match(SwagLangParser.GT)
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

        def map_type(self):
            return self.getTypedRuleContext(SwagLangParser.Map_typeContext,0)


        def set_type(self):
            return self.getTypedRuleContext(SwagLangParser.Set_typeContext,0)


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
        self.enterRule(localctx, 30, self.RULE_type_ann)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 193
                self.match(SwagLangParser.TYPE)
                pass
            elif token in [4]:
                self.state = 194
                self.map_type()
                pass
            elif token in [5]:
                self.state = 195
                self.set_type()
                pass
            elif token in [21]:
                self.state = 196
                self.match(SwagLangParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 199
                self.match(SwagLangParser.L_BRACKET)
                self.state = 200
                self.match(SwagLangParser.R_BRACKET)
                self.state = 205
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
        self.enterRule(localctx, 32, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(SwagLangParser.INTERFACE)
            self.state = 207
            self.match(SwagLangParser.IDENT)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 208
                self.match(SwagLangParser.EXTENDS)
                self.state = 209
                self.match(SwagLangParser.IDENT)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 210
                    self.match(SwagLangParser.COMMA)
                    self.state = 211
                    self.match(SwagLangParser.IDENT)
                    self.state = 216
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 219
            self.match(SwagLangParser.L_CURLY)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 220
                self.match(SwagLangParser.NWLN)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 226
                self.interface_field()
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 228 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 227
                            self.match(SwagLangParser.NWLN)
                            self.state = 230 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==60):
                                break

                        self.state = 232
                        self.interface_field() 
                    self.state = 237
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 238
                    self.match(SwagLangParser.NWLN)
                    self.state = 243
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 246
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
        self.enterRule(localctx, 34, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(SwagLangParser.IDENT)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 249
                self.match(SwagLangParser.QUESTION)


            self.state = 252
            self.match(SwagLangParser.COLUMN)
            self.state = 253
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

        def NULL(self):
            return self.getToken(SwagLangParser.NULL, 0)

        def array(self):
            return self.getTypedRuleContext(SwagLangParser.ArrayContext,0)


        def array_alloc(self):
            return self.getTypedRuleContext(SwagLangParser.Array_allocContext,0)


        def map_(self):
            return self.getTypedRuleContext(SwagLangParser.MapContext,0)


        def set_(self):
            return self.getTypedRuleContext(SwagLangParser.SetContext,0)


        def struct(self):
            return self.getTypedRuleContext(SwagLangParser.StructContext,0)


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
        self.enterRule(localctx, 36, self.RULE_data)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(SwagLangParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(SwagLangParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(SwagLangParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.match(SwagLangParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 259
                self.match(SwagLangParser.NULL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 260
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 261
                self.array_alloc()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 262
                self.map_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 263
                self.set_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 264
                self.struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(SwagLangParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(SwagLangParser.R_BRACKET, 0)

        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

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
            return SwagLangParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = SwagLangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(SwagLangParser.L_BRACKET)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 268
                    self.match(SwagLangParser.NWLN) 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080868317561356352) != 0):
                self.state = 274
                self.expr(0)
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 275
                        self.match(SwagLangParser.COMMA)
                        self.state = 279
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 276
                            self.match(SwagLangParser.NWLN)
                            self.state = 281
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 282
                        self.expr(0) 
                    self.state = 287
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 288
                    self.match(SwagLangParser.COMMA)




            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 293
                self.match(SwagLangParser.NWLN)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 299
            self.match(SwagLangParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_allocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(SwagLangParser.TYPE, 0)

        def L_BRACKET(self):
            return self.getToken(SwagLangParser.L_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def R_BRACKET(self):
            return self.getToken(SwagLangParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_array_alloc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_alloc" ):
                listener.enterArray_alloc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_alloc" ):
                listener.exitArray_alloc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_alloc" ):
                return visitor.visitArray_alloc(self)
            else:
                return visitor.visitChildren(self)




    def array_alloc(self):

        localctx = SwagLangParser.Array_allocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_alloc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(SwagLangParser.TYPE)
            self.state = 302
            self.match(SwagLangParser.L_BRACKET)
            self.state = 303
            self.expr(0)
            self.state = 304
            self.match(SwagLangParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.L_CURLY)
            else:
                return self.getToken(SwagLangParser.L_CURLY, i)

        def R_CURLY(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.R_CURLY)
            else:
                return self.getToken(SwagLangParser.R_CURLY, i)

        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

        def map_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Map_fieldContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Map_fieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_map

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap" ):
                listener.enterMap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap" ):
                listener.exitMap(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap" ):
                return visitor.visitMap(self)
            else:
                return visitor.visitChildren(self)




    def map_(self):

        localctx = SwagLangParser.MapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_map)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(SwagLangParser.L_CURLY)
            self.state = 307
            self.match(SwagLangParser.L_CURLY)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 308
                    self.match(SwagLangParser.NWLN) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080868317561356352) != 0):
                self.state = 314
                self.map_field()
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 315
                        self.match(SwagLangParser.COMMA)
                        self.state = 319
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 316
                            self.match(SwagLangParser.NWLN)
                            self.state = 321
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 322
                        self.map_field() 
                    self.state = 327
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 328
                    self.match(SwagLangParser.COMMA)




            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 333
                self.match(SwagLangParser.NWLN)
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 339
            self.match(SwagLangParser.R_CURLY)
            self.state = 340
            self.match(SwagLangParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def getRuleIndex(self):
            return SwagLangParser.RULE_map_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_field" ):
                listener.enterMap_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_field" ):
                listener.exitMap_field(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_field" ):
                return visitor.visitMap_field(self)
            else:
                return visitor.visitChildren(self)




    def map_field(self):

        localctx = SwagLangParser.Map_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_map_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.expr(0)
            self.state = 343
            self.match(SwagLangParser.COLUMN)
            self.state = 344
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET_START(self):
            return self.getToken(SwagLangParser.SET_START, 0)

        def R_BRACKET(self):
            return self.getToken(SwagLangParser.R_BRACKET, 0)

        def NWLN(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.NWLN)
            else:
                return self.getToken(SwagLangParser.NWLN, i)

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
            return SwagLangParser.RULE_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet" ):
                listener.enterSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet" ):
                listener.exitSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet" ):
                return visitor.visitSet(self)
            else:
                return visitor.visitChildren(self)




    def set_(self):

        localctx = SwagLangParser.SetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(SwagLangParser.SET_START)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 347
                    self.match(SwagLangParser.NWLN) 
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080868317561356352) != 0):
                self.state = 353
                self.expr(0)
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 354
                        self.match(SwagLangParser.COMMA)
                        self.state = 358
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 355
                            self.match(SwagLangParser.NWLN)
                            self.state = 360
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 361
                        self.expr(0) 
                    self.state = 366
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 367
                    self.match(SwagLangParser.COMMA)




            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 372
                self.match(SwagLangParser.NWLN)
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 378
            self.match(SwagLangParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructContext(ParserRuleContext):
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

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.Struct_fieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SwagLangParser.COMMA)
            else:
                return self.getToken(SwagLangParser.COMMA, i)

        def getRuleIndex(self):
            return SwagLangParser.RULE_struct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct" ):
                listener.enterStruct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct" ):
                listener.exitStruct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct" ):
                return visitor.visitStruct(self)
            else:
                return visitor.visitChildren(self)




    def struct(self):

        localctx = SwagLangParser.StructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(SwagLangParser.L_CURLY)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 381
                    self.match(SwagLangParser.NWLN) 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 387
                self.struct_field()
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 388
                        self.match(SwagLangParser.COMMA)
                        self.state = 392
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 389
                            self.match(SwagLangParser.NWLN)
                            self.state = 394
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 395
                        self.struct_field() 
                    self.state = 400
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 401
                    self.match(SwagLangParser.COMMA)




            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 406
                self.match(SwagLangParser.NWLN)
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 412
            self.match(SwagLangParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SwagLangParser.IDENT, 0)

        def COLUMN(self):
            return self.getToken(SwagLangParser.COLUMN, 0)

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwagLangParser.RULE_struct_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_field" ):
                listener.enterStruct_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_field" ):
                listener.exitStruct_field(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = SwagLangParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(SwagLangParser.IDENT)
            self.state = 415
            self.match(SwagLangParser.COLUMN)
            self.state = 416
            self.expr(0)
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
        self.enterRule(localctx, 52, self.RULE_no_acs_mode_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(SwagLangParser.IDENT)
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 419
                self.match(SwagLangParser.COLUMN)
                self.state = 420
                self.type_ann()


            self.state = 423
            self.match(SwagLangParser.ASSIGN)
            self.state = 424
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwagLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwagLangParser.ExprContext,i)


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
        self.enterRule(localctx, 54, self.RULE_var_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(SwagLangParser.IDENT)
            self.state = 435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 433
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [28]:
                        self.state = 427
                        self.match(SwagLangParser.L_BRACKET)
                        self.state = 428
                        self.expr(0)
                        self.state = 429
                        self.match(SwagLangParser.R_BRACKET)
                        pass
                    elif token in [32]:
                        self.state = 431
                        self.match(SwagLangParser.DOT)
                        self.state = 432
                        self.var_ref()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 437
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 439
                self.match(SwagLangParser.IDENT)
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 440
                    self.match(SwagLangParser.COLUMN)
                    self.state = 441
                    self.type_ann()


                self.state = 444
                self.match(SwagLangParser.ASSIGN)
                self.state = 445
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 447
                self.match(SwagLangParser.IDENT)
                self.state = 450 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 448
                    self.match(SwagLangParser.COMMA)
                    self.state = 449
                    self.match(SwagLangParser.IDENT)
                    self.state = 452 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                self.state = 454
                self.match(SwagLangParser.ASSIGN)
                self.state = 455
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
        self.enterRule(localctx, 58, self.RULE_var_assign)
        self._la = 0 # Token type
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.var_ref()
                self.state = 459
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 460
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.var_ref()
                self.state = 465 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 463
                    self.match(SwagLangParser.COMMA)
                    self.state = 464
                    self.var_ref()
                    self.state = 467 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                self.state = 469
                self.match(SwagLangParser.ASSIGN)
                self.state = 470
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
        self.enterRule(localctx, 60, self.RULE_conditional_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
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
        self.enterRule(localctx, 62, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
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
        self.enterRule(localctx, 64, self.RULE_loop)
        try:
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.for_loop()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.while_loop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 480
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
        self.enterRule(localctx, 66, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(SwagLangParser.WHILE)
            self.state = 484
            self.condition()
            self.state = 485
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
        self.enterRule(localctx, 68, self.RULE_do_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(SwagLangParser.DO)
            self.state = 488
            self.loop_body()
            self.state = 489
            self.match(SwagLangParser.WHILE)
            self.state = 490
            self.match(SwagLangParser.L_PAREN)
            self.state = 491
            self.condition()
            self.state = 492
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


        def var_assign(self):
            return self.getTypedRuleContext(SwagLangParser.Var_assignContext,0)


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
        self.enterRule(localctx, 70, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 494
                self.match(SwagLangParser.FOR)

                self.state = 496
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 495
                    self.no_acs_mode_var_decl()


                self.state = 498
                self.match(SwagLangParser.SEMICOL)
                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080868317561356352) != 0):
                    self.state = 499
                    self.condition()


                self.state = 502
                self.match(SwagLangParser.SEMICOL)
                self.state = 505
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 503
                    self.var_assign()

                elif la_ == 2:
                    self.state = 504
                    self.expr(0)


                pass

            elif la_ == 2:
                self.state = 507
                self.forin()
                pass


            self.state = 510
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

        def expr(self):
            return self.getTypedRuleContext(SwagLangParser.ExprContext,0)


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
        self.enterRule(localctx, 72, self.RULE_forin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(SwagLangParser.FOR)
            self.state = 513
            self.match(SwagLangParser.IDENT)
            self.state = 514
            self.match(SwagLangParser.IN)
            self.state = 515
            self.expr(0)
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
        self.enterRule(localctx, 74, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(SwagLangParser.IF)
            self.state = 518
            self.condition()
            self.state = 519
            self.conditional_body()
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 520
                self.match(SwagLangParser.ELSE_IF)
                self.state = 521
                self.condition()
                self.state = 522
                self.conditional_body()
                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 529
                self.match(SwagLangParser.ELSE)
                self.state = 530
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
        self.enterRule(localctx, 76, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
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

        def MINUS(self):
            return self.getToken(SwagLangParser.MINUS, 0)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 536
                self.match(SwagLangParser.L_PAREN)
                self.state = 537
                self.expr(0)
                self.state = 538
                self.match(SwagLangParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 540
                self.data()
                pass

            elif la_ == 3:
                self.state = 541
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 542
                self.var_ref()
                pass

            elif la_ == 5:
                self.state = 543
                self.var_ref()
                self.state = 544
                _la = self._input.LA(1)
                if not(_la==47 or _la==48):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.state = 546
                self.match(SwagLangParser.NOT)
                self.state = 547
                self.expr(9)
                pass

            elif la_ == 7:
                self.state = 548
                self.match(SwagLangParser.MINUS)
                self.state = 549
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 578
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 576
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 552
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 553
                        self.match(SwagLangParser.EXP)
                        self.state = 554
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 555
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 556
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123145302310912) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 557
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 558
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 559
                        _la = self._input.LA(1)
                        if not(_la==55 or _la==56):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 560
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 561
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 562
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35465847065542656) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 563
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 564
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 565
                        self.match(SwagLangParser.AND)
                        self.state = 566
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 567
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 568
                        self.match(SwagLangParser.OR)
                        self.state = 569
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 570
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 571
                        self.match(SwagLangParser.QUESTION)
                        self.state = 572
                        self.expr(0)
                        self.state = 573
                        self.match(SwagLangParser.COLUMN)
                        self.state = 574
                        self.expr(2)
                        pass

             
                self.state = 580
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(SwagLangParser.IDENT)
            self.state = 582
            self.match(SwagLangParser.L_PAREN)
            self.state = 583
            self.params()
            self.state = 584
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
        self.enterRule(localctx, 82, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(SwagLangParser.IDENT)
            self.state = 587
            self.match(SwagLangParser.COLUMN)
            self.state = 588
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
        self.enterRule(localctx, 84, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080868317561356352) != 0):
                self.state = 590
                self.expr(0)
                self.state = 595
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 591
                        self.match(SwagLangParser.COMMA)
                        self.state = 592
                        self.expr(0) 
                    self.state = 597
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

                self.state = 599
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 598
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
        self._predicates[39] = self.expr_sempred
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
         




