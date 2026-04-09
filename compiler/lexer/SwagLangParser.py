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
        4,1,63,595,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,1,0,1,0,1,1,1,1,5,1,90,8,1,10,1,12,1,93,
        9,1,1,2,1,2,1,3,1,3,1,3,3,3,100,8,3,1,4,1,4,1,4,1,4,5,4,106,8,4,
        10,4,12,4,109,9,4,1,4,1,4,1,5,3,5,114,8,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,127,8,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,
        10,1,10,1,10,1,10,5,10,140,8,10,10,10,12,10,143,9,10,3,10,145,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,153,8,11,10,11,12,11,156,9,
        11,1,11,3,11,159,8,11,3,11,161,8,11,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,4,12,172,8,12,11,12,12,12,173,1,12,1,12,3,12,178,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,3,15,196,8,15,1,15,1,15,5,15,200,8,15,10,15,
        12,15,203,9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,211,8,16,10,16,
        12,16,214,9,16,3,16,216,8,16,1,16,1,16,5,16,220,8,16,10,16,12,16,
        223,9,16,1,16,1,16,4,16,227,8,16,11,16,12,16,228,1,16,5,16,232,8,
        16,10,16,12,16,235,9,16,1,16,5,16,238,8,16,10,16,12,16,241,9,16,
        3,16,243,8,16,1,16,1,16,1,17,1,17,3,17,249,8,17,1,17,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,263,8,18,1,19,1,
        19,5,19,267,8,19,10,19,12,19,270,9,19,1,19,1,19,1,19,5,19,275,8,
        19,10,19,12,19,278,9,19,1,19,5,19,281,8,19,10,19,12,19,284,9,19,
        1,19,3,19,287,8,19,3,19,289,8,19,1,19,5,19,292,8,19,10,19,12,19,
        295,9,19,1,19,1,19,1,20,1,20,1,20,5,20,302,8,20,10,20,12,20,305,
        9,20,1,20,1,20,1,20,5,20,310,8,20,10,20,12,20,313,9,20,1,20,5,20,
        316,8,20,10,20,12,20,319,9,20,1,20,3,20,322,8,20,3,20,324,8,20,1,
        20,5,20,327,8,20,10,20,12,20,330,9,20,1,20,1,20,1,20,1,21,1,21,1,
        21,1,21,1,22,1,22,5,22,341,8,22,10,22,12,22,344,9,22,1,22,1,22,1,
        22,5,22,349,8,22,10,22,12,22,352,9,22,1,22,5,22,355,8,22,10,22,12,
        22,358,9,22,1,22,3,22,361,8,22,3,22,363,8,22,1,22,5,22,366,8,22,
        10,22,12,22,369,9,22,1,22,1,22,1,23,1,23,5,23,375,8,23,10,23,12,
        23,378,9,23,1,23,1,23,1,23,5,23,383,8,23,10,23,12,23,386,9,23,1,
        23,5,23,389,8,23,10,23,12,23,392,9,23,1,23,3,23,395,8,23,3,23,397,
        8,23,1,23,5,23,400,8,23,10,23,12,23,403,9,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,3,25,414,8,25,1,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,5,26,426,8,26,10,26,12,26,429,9,26,1,27,
        1,27,1,27,1,27,3,27,435,8,27,1,27,1,27,1,27,1,27,1,27,1,27,4,27,
        443,8,27,11,27,12,27,444,1,27,1,27,3,27,449,8,27,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,4,28,458,8,28,11,28,12,28,459,1,28,1,28,1,28,
        3,28,465,8,28,1,29,1,29,1,30,1,30,1,31,1,31,1,31,3,31,474,8,31,1,
        32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,3,
        34,489,8,34,1,34,1,34,3,34,493,8,34,1,34,1,34,3,34,497,8,34,1,34,
        3,34,500,8,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,3,35,509,8,35,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,5,36,518,8,36,10,36,12,36,521,9,
        36,1,36,1,36,3,36,525,8,36,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,542,8,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,5,38,568,8,38,10,38,12,
        38,571,9,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,
        41,1,41,5,41,585,8,41,10,41,12,41,588,9,41,1,41,3,41,591,8,41,3,
        41,593,8,41,1,41,0,1,76,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,0,5,1,0,34,39,1,0,47,48,1,0,44,46,1,0,55,56,1,
        0,49,54,652,0,84,1,0,0,0,2,91,1,0,0,0,4,94,1,0,0,0,6,99,1,0,0,0,
        8,101,1,0,0,0,10,113,1,0,0,0,12,126,1,0,0,0,14,128,1,0,0,0,16,131,
        1,0,0,0,18,133,1,0,0,0,20,135,1,0,0,0,22,146,1,0,0,0,24,177,1,0,
        0,0,26,179,1,0,0,0,28,186,1,0,0,0,30,195,1,0,0,0,32,204,1,0,0,0,
        34,246,1,0,0,0,36,262,1,0,0,0,38,264,1,0,0,0,40,298,1,0,0,0,42,334,
        1,0,0,0,44,338,1,0,0,0,46,372,1,0,0,0,48,406,1,0,0,0,50,410,1,0,
        0,0,52,418,1,0,0,0,54,448,1,0,0,0,56,464,1,0,0,0,58,466,1,0,0,0,
        60,468,1,0,0,0,62,473,1,0,0,0,64,475,1,0,0,0,66,479,1,0,0,0,68,499,
        1,0,0,0,70,503,1,0,0,0,72,510,1,0,0,0,74,526,1,0,0,0,76,541,1,0,
        0,0,78,572,1,0,0,0,80,577,1,0,0,0,82,592,1,0,0,0,84,85,3,2,1,0,85,
        86,5,0,0,1,86,1,1,0,0,0,87,90,3,4,2,0,88,90,5,60,0,0,89,87,1,0,0,
        0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,3,1,
        0,0,0,93,91,1,0,0,0,94,95,3,6,3,0,95,5,1,0,0,0,96,100,3,22,11,0,
        97,100,3,54,27,0,98,100,3,32,16,0,99,96,1,0,0,0,99,97,1,0,0,0,99,
        98,1,0,0,0,100,7,1,0,0,0,101,107,5,26,0,0,102,103,3,10,5,0,103,104,
        5,60,0,0,104,106,1,0,0,0,105,102,1,0,0,0,106,109,1,0,0,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,
        5,27,0,0,111,9,1,0,0,0,112,114,3,12,6,0,113,112,1,0,0,0,113,114,
        1,0,0,0,114,11,1,0,0,0,115,127,3,22,11,0,116,127,3,56,28,0,117,127,
        3,78,39,0,118,127,3,54,27,0,119,127,3,62,31,0,120,127,3,72,36,0,
        121,127,3,16,8,0,122,127,3,18,9,0,123,127,3,20,10,0,124,127,3,14,
        7,0,125,127,3,76,38,0,126,115,1,0,0,0,126,116,1,0,0,0,126,117,1,
        0,0,0,126,118,1,0,0,0,126,119,1,0,0,0,126,120,1,0,0,0,126,121,1,
        0,0,0,126,122,1,0,0,0,126,123,1,0,0,0,126,124,1,0,0,0,126,125,1,
        0,0,0,127,13,1,0,0,0,128,129,5,17,0,0,129,130,3,76,38,0,130,15,1,
        0,0,0,131,132,5,14,0,0,132,17,1,0,0,0,133,134,5,15,0,0,134,19,1,
        0,0,0,135,144,5,16,0,0,136,141,3,76,38,0,137,138,5,31,0,0,138,140,
        3,76,38,0,139,137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,144,136,1,0,0,0,144,145,
        1,0,0,0,145,21,1,0,0,0,146,147,3,24,12,0,147,148,5,21,0,0,148,160,
        5,24,0,0,149,154,3,80,40,0,150,151,5,31,0,0,151,153,3,80,40,0,152,
        150,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,
        158,1,0,0,0,156,154,1,0,0,0,157,159,5,31,0,0,158,157,1,0,0,0,158,
        159,1,0,0,0,159,161,1,0,0,0,160,149,1,0,0,0,160,161,1,0,0,0,161,
        162,1,0,0,0,162,163,5,25,0,0,163,164,3,8,4,0,164,23,1,0,0,0,165,
        178,3,30,15,0,166,178,5,3,0,0,167,168,5,24,0,0,168,171,3,30,15,0,
        169,170,5,31,0,0,170,172,3,30,15,0,171,169,1,0,0,0,172,173,1,0,0,
        0,173,171,1,0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,176,5,25,0,
        0,176,178,1,0,0,0,177,165,1,0,0,0,177,166,1,0,0,0,177,167,1,0,0,
        0,178,25,1,0,0,0,179,180,5,4,0,0,180,181,5,50,0,0,181,182,3,30,15,
        0,182,183,5,31,0,0,183,184,3,30,15,0,184,185,5,49,0,0,185,27,1,0,
        0,0,186,187,5,5,0,0,187,188,5,50,0,0,188,189,3,30,15,0,189,190,5,
        49,0,0,190,29,1,0,0,0,191,196,5,6,0,0,192,196,3,26,13,0,193,196,
        3,28,14,0,194,196,5,21,0,0,195,191,1,0,0,0,195,192,1,0,0,0,195,193,
        1,0,0,0,195,194,1,0,0,0,196,201,1,0,0,0,197,198,5,28,0,0,198,200,
        5,29,0,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,
        1,0,0,0,202,31,1,0,0,0,203,201,1,0,0,0,204,205,5,1,0,0,205,215,5,
        21,0,0,206,207,5,2,0,0,207,212,5,21,0,0,208,209,5,31,0,0,209,211,
        5,21,0,0,210,208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,215,206,1,0,0,0,215,216,
        1,0,0,0,216,217,1,0,0,0,217,221,5,26,0,0,218,220,5,60,0,0,219,218,
        1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,242,
        1,0,0,0,223,221,1,0,0,0,224,233,3,34,17,0,225,227,5,60,0,0,226,225,
        1,0,0,0,227,228,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,230,
        1,0,0,0,230,232,3,34,17,0,231,226,1,0,0,0,232,235,1,0,0,0,233,231,
        1,0,0,0,233,234,1,0,0,0,234,239,1,0,0,0,235,233,1,0,0,0,236,238,
        5,60,0,0,237,236,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,
        1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,242,224,1,0,0,0,242,243,
        1,0,0,0,243,244,1,0,0,0,244,245,5,27,0,0,245,33,1,0,0,0,246,248,
        5,21,0,0,247,249,5,30,0,0,248,247,1,0,0,0,248,249,1,0,0,0,249,250,
        1,0,0,0,250,251,5,22,0,0,251,252,3,30,15,0,252,35,1,0,0,0,253,263,
        5,58,0,0,254,263,5,57,0,0,255,263,5,59,0,0,256,263,5,19,0,0,257,
        263,5,20,0,0,258,263,3,38,19,0,259,263,3,40,20,0,260,263,3,44,22,
        0,261,263,3,46,23,0,262,253,1,0,0,0,262,254,1,0,0,0,262,255,1,0,
        0,0,262,256,1,0,0,0,262,257,1,0,0,0,262,258,1,0,0,0,262,259,1,0,
        0,0,262,260,1,0,0,0,262,261,1,0,0,0,263,37,1,0,0,0,264,268,5,28,
        0,0,265,267,5,60,0,0,266,265,1,0,0,0,267,270,1,0,0,0,268,266,1,0,
        0,0,268,269,1,0,0,0,269,288,1,0,0,0,270,268,1,0,0,0,271,282,3,76,
        38,0,272,276,5,31,0,0,273,275,5,60,0,0,274,273,1,0,0,0,275,278,1,
        0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,279,1,0,0,0,278,276,1,
        0,0,0,279,281,3,76,38,0,280,272,1,0,0,0,281,284,1,0,0,0,282,280,
        1,0,0,0,282,283,1,0,0,0,283,286,1,0,0,0,284,282,1,0,0,0,285,287,
        5,31,0,0,286,285,1,0,0,0,286,287,1,0,0,0,287,289,1,0,0,0,288,271,
        1,0,0,0,288,289,1,0,0,0,289,293,1,0,0,0,290,292,5,60,0,0,291,290,
        1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,296,
        1,0,0,0,295,293,1,0,0,0,296,297,5,29,0,0,297,39,1,0,0,0,298,299,
        5,26,0,0,299,303,5,26,0,0,300,302,5,60,0,0,301,300,1,0,0,0,302,305,
        1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,323,1,0,0,0,305,303,
        1,0,0,0,306,317,3,42,21,0,307,311,5,31,0,0,308,310,5,60,0,0,309,
        308,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,
        314,1,0,0,0,313,311,1,0,0,0,314,316,3,42,21,0,315,307,1,0,0,0,316,
        319,1,0,0,0,317,315,1,0,0,0,317,318,1,0,0,0,318,321,1,0,0,0,319,
        317,1,0,0,0,320,322,5,31,0,0,321,320,1,0,0,0,321,322,1,0,0,0,322,
        324,1,0,0,0,323,306,1,0,0,0,323,324,1,0,0,0,324,328,1,0,0,0,325,
        327,5,60,0,0,326,325,1,0,0,0,327,330,1,0,0,0,328,326,1,0,0,0,328,
        329,1,0,0,0,329,331,1,0,0,0,330,328,1,0,0,0,331,332,5,27,0,0,332,
        333,5,27,0,0,333,41,1,0,0,0,334,335,3,76,38,0,335,336,5,22,0,0,336,
        337,3,76,38,0,337,43,1,0,0,0,338,342,5,33,0,0,339,341,5,60,0,0,340,
        339,1,0,0,0,341,344,1,0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,
        362,1,0,0,0,344,342,1,0,0,0,345,356,3,76,38,0,346,350,5,31,0,0,347,
        349,5,60,0,0,348,347,1,0,0,0,349,352,1,0,0,0,350,348,1,0,0,0,350,
        351,1,0,0,0,351,353,1,0,0,0,352,350,1,0,0,0,353,355,3,76,38,0,354,
        346,1,0,0,0,355,358,1,0,0,0,356,354,1,0,0,0,356,357,1,0,0,0,357,
        360,1,0,0,0,358,356,1,0,0,0,359,361,5,31,0,0,360,359,1,0,0,0,360,
        361,1,0,0,0,361,363,1,0,0,0,362,345,1,0,0,0,362,363,1,0,0,0,363,
        367,1,0,0,0,364,366,5,60,0,0,365,364,1,0,0,0,366,369,1,0,0,0,367,
        365,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,0,369,367,1,0,0,0,370,
        371,5,29,0,0,371,45,1,0,0,0,372,376,5,26,0,0,373,375,5,60,0,0,374,
        373,1,0,0,0,375,378,1,0,0,0,376,374,1,0,0,0,376,377,1,0,0,0,377,
        396,1,0,0,0,378,376,1,0,0,0,379,390,3,48,24,0,380,384,5,31,0,0,381,
        383,5,60,0,0,382,381,1,0,0,0,383,386,1,0,0,0,384,382,1,0,0,0,384,
        385,1,0,0,0,385,387,1,0,0,0,386,384,1,0,0,0,387,389,3,48,24,0,388,
        380,1,0,0,0,389,392,1,0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,
        394,1,0,0,0,392,390,1,0,0,0,393,395,5,31,0,0,394,393,1,0,0,0,394,
        395,1,0,0,0,395,397,1,0,0,0,396,379,1,0,0,0,396,397,1,0,0,0,397,
        401,1,0,0,0,398,400,5,60,0,0,399,398,1,0,0,0,400,403,1,0,0,0,401,
        399,1,0,0,0,401,402,1,0,0,0,402,404,1,0,0,0,403,401,1,0,0,0,404,
        405,5,27,0,0,405,47,1,0,0,0,406,407,5,21,0,0,407,408,5,22,0,0,408,
        409,3,76,38,0,409,49,1,0,0,0,410,413,5,21,0,0,411,412,5,22,0,0,412,
        414,3,30,15,0,413,411,1,0,0,0,413,414,1,0,0,0,414,415,1,0,0,0,415,
        416,5,34,0,0,416,417,3,76,38,0,417,51,1,0,0,0,418,427,5,21,0,0,419,
        420,5,28,0,0,420,421,3,76,38,0,421,422,5,29,0,0,422,426,1,0,0,0,
        423,424,5,32,0,0,424,426,3,52,26,0,425,419,1,0,0,0,425,423,1,0,0,
        0,426,429,1,0,0,0,427,425,1,0,0,0,427,428,1,0,0,0,428,53,1,0,0,0,
        429,427,1,0,0,0,430,431,5,18,0,0,431,434,5,21,0,0,432,433,5,22,0,
        0,433,435,3,30,15,0,434,432,1,0,0,0,434,435,1,0,0,0,435,436,1,0,
        0,0,436,437,5,34,0,0,437,449,3,76,38,0,438,439,5,18,0,0,439,442,
        5,21,0,0,440,441,5,31,0,0,441,443,5,21,0,0,442,440,1,0,0,0,443,444,
        1,0,0,0,444,442,1,0,0,0,444,445,1,0,0,0,445,446,1,0,0,0,446,447,
        5,34,0,0,447,449,3,78,39,0,448,430,1,0,0,0,448,438,1,0,0,0,449,55,
        1,0,0,0,450,451,3,52,26,0,451,452,7,0,0,0,452,453,3,76,38,0,453,
        465,1,0,0,0,454,457,3,52,26,0,455,456,5,31,0,0,456,458,3,52,26,0,
        457,455,1,0,0,0,458,459,1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,
        460,461,1,0,0,0,461,462,5,34,0,0,462,463,3,78,39,0,463,465,1,0,0,
        0,464,450,1,0,0,0,464,454,1,0,0,0,465,57,1,0,0,0,466,467,3,8,4,0,
        467,59,1,0,0,0,468,469,3,8,4,0,469,61,1,0,0,0,470,474,3,68,34,0,
        471,474,3,64,32,0,472,474,3,66,33,0,473,470,1,0,0,0,473,471,1,0,
        0,0,473,472,1,0,0,0,474,63,1,0,0,0,475,476,5,12,0,0,476,477,3,74,
        37,0,477,478,3,60,30,0,478,65,1,0,0,0,479,480,5,13,0,0,480,481,3,
        60,30,0,481,482,5,12,0,0,482,483,5,24,0,0,483,484,3,74,37,0,484,
        485,5,25,0,0,485,67,1,0,0,0,486,488,5,10,0,0,487,489,3,50,25,0,488,
        487,1,0,0,0,488,489,1,0,0,0,489,490,1,0,0,0,490,492,5,23,0,0,491,
        493,3,74,37,0,492,491,1,0,0,0,492,493,1,0,0,0,493,494,1,0,0,0,494,
        496,5,23,0,0,495,497,3,76,38,0,496,495,1,0,0,0,496,497,1,0,0,0,497,
        500,1,0,0,0,498,500,3,70,35,0,499,486,1,0,0,0,499,498,1,0,0,0,500,
        501,1,0,0,0,501,502,3,60,30,0,502,69,1,0,0,0,503,504,5,10,0,0,504,
        505,5,21,0,0,505,508,5,11,0,0,506,509,3,78,39,0,507,509,3,52,26,
        0,508,506,1,0,0,0,508,507,1,0,0,0,509,71,1,0,0,0,510,511,5,7,0,0,
        511,512,3,74,37,0,512,519,3,58,29,0,513,514,5,8,0,0,514,515,3,74,
        37,0,515,516,3,58,29,0,516,518,1,0,0,0,517,513,1,0,0,0,518,521,1,
        0,0,0,519,517,1,0,0,0,519,520,1,0,0,0,520,524,1,0,0,0,521,519,1,
        0,0,0,522,523,5,9,0,0,523,525,3,58,29,0,524,522,1,0,0,0,524,525,
        1,0,0,0,525,73,1,0,0,0,526,527,3,76,38,0,527,75,1,0,0,0,528,529,
        6,38,-1,0,529,530,5,24,0,0,530,531,3,76,38,0,531,532,5,25,0,0,532,
        542,1,0,0,0,533,542,3,36,18,0,534,542,3,78,39,0,535,542,3,52,26,
        0,536,537,3,52,26,0,537,538,7,1,0,0,538,542,1,0,0,0,539,540,5,42,
        0,0,540,542,3,76,38,8,541,528,1,0,0,0,541,533,1,0,0,0,541,534,1,
        0,0,0,541,535,1,0,0,0,541,536,1,0,0,0,541,539,1,0,0,0,542,569,1,
        0,0,0,543,544,10,7,0,0,544,545,5,43,0,0,545,568,3,76,38,7,546,547,
        10,6,0,0,547,548,7,2,0,0,548,568,3,76,38,7,549,550,10,5,0,0,550,
        551,7,3,0,0,551,568,3,76,38,6,552,553,10,4,0,0,553,554,7,4,0,0,554,
        568,3,76,38,5,555,556,10,3,0,0,556,557,5,40,0,0,557,568,3,76,38,
        4,558,559,10,2,0,0,559,560,5,41,0,0,560,568,3,76,38,3,561,562,10,
        1,0,0,562,563,5,30,0,0,563,564,3,76,38,0,564,565,5,22,0,0,565,566,
        3,76,38,2,566,568,1,0,0,0,567,543,1,0,0,0,567,546,1,0,0,0,567,549,
        1,0,0,0,567,552,1,0,0,0,567,555,1,0,0,0,567,558,1,0,0,0,567,561,
        1,0,0,0,568,571,1,0,0,0,569,567,1,0,0,0,569,570,1,0,0,0,570,77,1,
        0,0,0,571,569,1,0,0,0,572,573,5,21,0,0,573,574,5,24,0,0,574,575,
        3,82,41,0,575,576,5,25,0,0,576,79,1,0,0,0,577,578,5,21,0,0,578,579,
        5,22,0,0,579,580,3,30,15,0,580,81,1,0,0,0,581,586,3,76,38,0,582,
        583,5,31,0,0,583,585,3,76,38,0,584,582,1,0,0,0,585,588,1,0,0,0,586,
        584,1,0,0,0,586,587,1,0,0,0,587,590,1,0,0,0,588,586,1,0,0,0,589,
        591,5,31,0,0,590,589,1,0,0,0,590,591,1,0,0,0,591,593,1,0,0,0,592,
        581,1,0,0,0,592,593,1,0,0,0,593,83,1,0,0,0,70,89,91,99,107,113,126,
        141,144,154,158,160,173,177,195,201,212,215,221,228,233,239,242,
        248,262,268,276,282,286,288,293,303,311,317,321,323,328,342,350,
        356,360,362,367,376,384,390,394,396,401,413,425,427,434,444,448,
        459,464,473,488,492,496,499,508,519,524,541,567,569,586,590,592
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
    RULE_map = 20
    RULE_map_field = 21
    RULE_set = 22
    RULE_struct = 23
    RULE_struct_field = 24
    RULE_no_acs_mode_var_decl = 25
    RULE_var_ref = 26
    RULE_var_decl = 27
    RULE_var_assign = 28
    RULE_conditional_body = 29
    RULE_loop_body = 30
    RULE_loop = 31
    RULE_while_loop = 32
    RULE_do_while_loop = 33
    RULE_for_loop = 34
    RULE_forin = 35
    RULE_conditional = 36
    RULE_condition = 37
    RULE_expr = 38
    RULE_func_call = 39
    RULE_param_decl = 40
    RULE_params = 41

    ruleNames =  [ "prog", "stmts", "stmt", "pure_stmt", "code_block", "func_stmt", 
                   "pure_func_stmt", "defer", "break", "continue", "return", 
                   "func_decl", "return_type", "map_type", "set_type", "type_ann", 
                   "interface_decl", "interface_field", "data", "array", 
                   "map", "map_field", "set", "struct", "struct_field", 
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
            self.state = 84
            self.stmts()
            self.state = 85
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
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921504625983610) != 0):
                self.state = 89
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 4, 5, 6, 18, 21, 24]:
                    self.state = 87
                    self.stmt()
                    pass
                elif token in [60]:
                    self.state = 88
                    self.match(SwagLangParser.NWLN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 93
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
            self.state = 94
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
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 21, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.func_decl()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.var_decl()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
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
            self.state = 101
            self.match(SwagLangParser.L_CURLY)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2161732228130796792) != 0):
                self.state = 102
                self.func_stmt()
                self.state = 103
                self.match(SwagLangParser.NWLN)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
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
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008810723523949816) != 0):
                self.state = 112
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.var_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.var_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 121
                self.break_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 122
                self.continue_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 123
                self.return_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 124
                self.defer()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 125
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
            self.state = 128
            self.match(SwagLangParser.DEFER)
            self.state = 129
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
            self.state = 131
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
            self.state = 133
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
            self.state = 135
            self.match(SwagLangParser.RETURN)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008810723523428352) != 0):
                self.state = 136
                self.expr(0)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 137
                    self.match(SwagLangParser.COMMA)
                    self.state = 138
                    self.expr(0)
                    self.state = 143
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
            self.state = 146
            self.return_type()
            self.state = 147
            self.match(SwagLangParser.IDENT)
            self.state = 148
            self.match(SwagLangParser.L_PAREN)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 149
                self.param_decl()
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 150
                        self.match(SwagLangParser.COMMA)
                        self.state = 151
                        self.param_decl() 
                    self.state = 156
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 157
                    self.match(SwagLangParser.COMMA)




            self.state = 162
            self.match(SwagLangParser.R_PAREN)
            self.state = 163
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
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.type_ann()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(SwagLangParser.VOID)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(SwagLangParser.L_PAREN)
                self.state = 168
                self.type_ann()
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 169
                    self.match(SwagLangParser.COMMA)
                    self.state = 170
                    self.type_ann()
                    self.state = 173 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                self.state = 175
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
            self.state = 179
            self.match(SwagLangParser.MAP)
            self.state = 180
            self.match(SwagLangParser.LT)
            self.state = 181
            self.type_ann()
            self.state = 182
            self.match(SwagLangParser.COMMA)
            self.state = 183
            self.type_ann()
            self.state = 184
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
            self.state = 186
            self.match(SwagLangParser.SET)
            self.state = 187
            self.match(SwagLangParser.LT)
            self.state = 188
            self.type_ann()
            self.state = 189
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 191
                self.match(SwagLangParser.TYPE)
                pass
            elif token in [4]:
                self.state = 192
                self.map_type()
                pass
            elif token in [5]:
                self.state = 193
                self.set_type()
                pass
            elif token in [21]:
                self.state = 194
                self.match(SwagLangParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 197
                self.match(SwagLangParser.L_BRACKET)
                self.state = 198
                self.match(SwagLangParser.R_BRACKET)
                self.state = 203
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
            self.state = 204
            self.match(SwagLangParser.INTERFACE)
            self.state = 205
            self.match(SwagLangParser.IDENT)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 206
                self.match(SwagLangParser.EXTENDS)
                self.state = 207
                self.match(SwagLangParser.IDENT)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 208
                    self.match(SwagLangParser.COMMA)
                    self.state = 209
                    self.match(SwagLangParser.IDENT)
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 217
            self.match(SwagLangParser.L_CURLY)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 218
                self.match(SwagLangParser.NWLN)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 224
                self.interface_field()
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 226 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 225
                            self.match(SwagLangParser.NWLN)
                            self.state = 228 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==60):
                                break

                        self.state = 230
                        self.interface_field() 
                    self.state = 235
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 236
                    self.match(SwagLangParser.NWLN)
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 244
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
            self.state = 246
            self.match(SwagLangParser.IDENT)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 247
                self.match(SwagLangParser.QUESTION)


            self.state = 250
            self.match(SwagLangParser.COLUMN)
            self.state = 251
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
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(SwagLangParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(SwagLangParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.match(SwagLangParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.match(SwagLangParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.match(SwagLangParser.NULL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 259
                self.map_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 260
                self.set_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 261
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
            self.state = 264
            self.match(SwagLangParser.L_BRACKET)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 265
                    self.match(SwagLangParser.NWLN) 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008810723523428352) != 0):
                self.state = 271
                self.expr(0)
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 272
                        self.match(SwagLangParser.COMMA)
                        self.state = 276
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 273
                            self.match(SwagLangParser.NWLN)
                            self.state = 278
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 279
                        self.expr(0) 
                    self.state = 284
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 285
                    self.match(SwagLangParser.COMMA)




            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 290
                self.match(SwagLangParser.NWLN)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
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
        self.enterRule(localctx, 40, self.RULE_map)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(SwagLangParser.L_CURLY)
            self.state = 299
            self.match(SwagLangParser.L_CURLY)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 300
                    self.match(SwagLangParser.NWLN) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008810723523428352) != 0):
                self.state = 306
                self.map_field()
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 307
                        self.match(SwagLangParser.COMMA)
                        self.state = 311
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 308
                            self.match(SwagLangParser.NWLN)
                            self.state = 313
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 314
                        self.map_field() 
                    self.state = 319
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 320
                    self.match(SwagLangParser.COMMA)




            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 325
                self.match(SwagLangParser.NWLN)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 331
            self.match(SwagLangParser.R_CURLY)
            self.state = 332
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
        self.enterRule(localctx, 42, self.RULE_map_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.expr(0)
            self.state = 335
            self.match(SwagLangParser.COLUMN)
            self.state = 336
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
        self.enterRule(localctx, 44, self.RULE_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(SwagLangParser.SET_START)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 339
                    self.match(SwagLangParser.NWLN) 
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008810723523428352) != 0):
                self.state = 345
                self.expr(0)
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 346
                        self.match(SwagLangParser.COMMA)
                        self.state = 350
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 347
                            self.match(SwagLangParser.NWLN)
                            self.state = 352
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 353
                        self.expr(0) 
                    self.state = 358
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 359
                    self.match(SwagLangParser.COMMA)




            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 364
                self.match(SwagLangParser.NWLN)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370
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
        self.enterRule(localctx, 46, self.RULE_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(SwagLangParser.L_CURLY)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 373
                    self.match(SwagLangParser.NWLN) 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 379
                self.struct_field()
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 380
                        self.match(SwagLangParser.COMMA)
                        self.state = 384
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==60:
                            self.state = 381
                            self.match(SwagLangParser.NWLN)
                            self.state = 386
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 387
                        self.struct_field() 
                    self.state = 392
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 393
                    self.match(SwagLangParser.COMMA)




            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 398
                self.match(SwagLangParser.NWLN)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 404
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
        self.enterRule(localctx, 48, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(SwagLangParser.IDENT)
            self.state = 407
            self.match(SwagLangParser.COLUMN)
            self.state = 408
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
        self.enterRule(localctx, 50, self.RULE_no_acs_mode_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(SwagLangParser.IDENT)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 411
                self.match(SwagLangParser.COLUMN)
                self.state = 412
                self.type_ann()


            self.state = 415
            self.match(SwagLangParser.ASSIGN)
            self.state = 416
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
        self.enterRule(localctx, 52, self.RULE_var_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(SwagLangParser.IDENT)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 425
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [28]:
                        self.state = 419
                        self.match(SwagLangParser.L_BRACKET)
                        self.state = 420
                        self.expr(0)
                        self.state = 421
                        self.match(SwagLangParser.R_BRACKET)
                        pass
                    elif token in [32]:
                        self.state = 423
                        self.match(SwagLangParser.DOT)
                        self.state = 424
                        self.var_ref()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 429
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
        self.enterRule(localctx, 54, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 431
                self.match(SwagLangParser.IDENT)
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 432
                    self.match(SwagLangParser.COLUMN)
                    self.state = 433
                    self.type_ann()


                self.state = 436
                self.match(SwagLangParser.ASSIGN)
                self.state = 437
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 439
                self.match(SwagLangParser.IDENT)
                self.state = 442 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 440
                    self.match(SwagLangParser.COMMA)
                    self.state = 441
                    self.match(SwagLangParser.IDENT)
                    self.state = 444 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                self.state = 446
                self.match(SwagLangParser.ASSIGN)
                self.state = 447
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
        self.enterRule(localctx, 56, self.RULE_var_assign)
        self._la = 0 # Token type
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.var_ref()
                self.state = 451
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 452
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.var_ref()
                self.state = 457 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 455
                    self.match(SwagLangParser.COMMA)
                    self.state = 456
                    self.var_ref()
                    self.state = 459 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                self.state = 461
                self.match(SwagLangParser.ASSIGN)
                self.state = 462
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
        self.enterRule(localctx, 58, self.RULE_conditional_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
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
        self.enterRule(localctx, 60, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
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
        self.enterRule(localctx, 62, self.RULE_loop)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.for_loop()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.while_loop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 472
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
        self.enterRule(localctx, 64, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(SwagLangParser.WHILE)
            self.state = 476
            self.condition()
            self.state = 477
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
        self.enterRule(localctx, 66, self.RULE_do_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(SwagLangParser.DO)
            self.state = 480
            self.loop_body()
            self.state = 481
            self.match(SwagLangParser.WHILE)
            self.state = 482
            self.match(SwagLangParser.L_PAREN)
            self.state = 483
            self.condition()
            self.state = 484
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
        self.enterRule(localctx, 68, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 486
                self.match(SwagLangParser.FOR)

                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 487
                    self.no_acs_mode_var_decl()


                self.state = 490
                self.match(SwagLangParser.SEMICOL)
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008810723523428352) != 0):
                    self.state = 491
                    self.condition()


                self.state = 494
                self.match(SwagLangParser.SEMICOL)
                self.state = 496
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 495
                    self.expr(0)


                pass

            elif la_ == 2:
                self.state = 498
                self.forin()
                pass


            self.state = 501
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
        self.enterRule(localctx, 70, self.RULE_forin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(SwagLangParser.FOR)
            self.state = 504
            self.match(SwagLangParser.IDENT)
            self.state = 505
            self.match(SwagLangParser.IN)
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 506
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 507
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
        self.enterRule(localctx, 72, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(SwagLangParser.IF)
            self.state = 511
            self.condition()
            self.state = 512
            self.conditional_body()
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 513
                self.match(SwagLangParser.ELSE_IF)
                self.state = 514
                self.condition()
                self.state = 515
                self.conditional_body()
                self.state = 521
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 522
                self.match(SwagLangParser.ELSE)
                self.state = 523
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
        self.enterRule(localctx, 74, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 529
                self.match(SwagLangParser.L_PAREN)
                self.state = 530
                self.expr(0)
                self.state = 531
                self.match(SwagLangParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 533
                self.data()
                pass

            elif la_ == 3:
                self.state = 534
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 535
                self.var_ref()
                pass

            elif la_ == 5:
                self.state = 536
                self.var_ref()
                self.state = 537
                _la = self._input.LA(1)
                if not(_la==47 or _la==48):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.state = 539
                self.match(SwagLangParser.NOT)
                self.state = 540
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 569
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 567
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 543
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 544
                        self.match(SwagLangParser.EXP)
                        self.state = 545
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 546
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 547
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123145302310912) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 548
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 549
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 550
                        _la = self._input.LA(1)
                        if not(_la==55 or _la==56):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 551
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 552
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 553
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35465847065542656) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 554
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 555
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 556
                        self.match(SwagLangParser.AND)
                        self.state = 557
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 558
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 559
                        self.match(SwagLangParser.OR)
                        self.state = 560
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 561
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 562
                        self.match(SwagLangParser.QUESTION)
                        self.state = 563
                        self.expr(0)
                        self.state = 564
                        self.match(SwagLangParser.COLUMN)
                        self.state = 565
                        self.expr(2)
                        pass

             
                self.state = 571
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(SwagLangParser.IDENT)
            self.state = 573
            self.match(SwagLangParser.L_PAREN)
            self.state = 574
            self.params()
            self.state = 575
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
        self.enterRule(localctx, 80, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.match(SwagLangParser.IDENT)
            self.state = 578
            self.match(SwagLangParser.COLUMN)
            self.state = 579
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
        self.enterRule(localctx, 82, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008810723523428352) != 0):
                self.state = 581
                self.expr(0)
                self.state = 586
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 582
                        self.match(SwagLangParser.COMMA)
                        self.state = 583
                        self.expr(0) 
                    self.state = 588
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

                self.state = 590
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 589
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
        self._predicates[38] = self.expr_sempred
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
         




