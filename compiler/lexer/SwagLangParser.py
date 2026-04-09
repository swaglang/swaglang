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
        4,1,62,590,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,1,0,1,1,1,1,5,1,88,8,1,10,1,12,1,91,9,1,1,2,1,
        2,1,3,1,3,1,3,3,3,98,8,3,1,4,1,4,1,4,1,4,5,4,104,8,4,10,4,12,4,107,
        9,4,1,4,1,4,1,5,3,5,112,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,124,8,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,5,9,135,8,9,
        10,9,12,9,138,9,9,3,9,140,8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,
        148,8,10,10,10,12,10,151,9,10,1,10,3,10,154,8,10,3,10,156,8,10,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,4,11,167,8,11,11,11,12,
        11,168,1,11,1,11,3,11,173,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,191,8,14,1,14,
        1,14,5,14,195,8,14,10,14,12,14,198,9,14,1,15,1,15,1,15,1,15,1,15,
        1,15,5,15,206,8,15,10,15,12,15,209,9,15,3,15,211,8,15,1,15,1,15,
        5,15,215,8,15,10,15,12,15,218,9,15,1,15,1,15,4,15,222,8,15,11,15,
        12,15,223,1,15,5,15,227,8,15,10,15,12,15,230,9,15,1,15,5,15,233,
        8,15,10,15,12,15,236,9,15,3,15,238,8,15,1,15,1,15,1,16,1,16,3,16,
        244,8,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,258,8,17,1,18,1,18,5,18,262,8,18,10,18,12,18,265,9,18,
        1,18,1,18,1,18,5,18,270,8,18,10,18,12,18,273,9,18,1,18,5,18,276,
        8,18,10,18,12,18,279,9,18,1,18,3,18,282,8,18,3,18,284,8,18,1,18,
        5,18,287,8,18,10,18,12,18,290,9,18,1,18,1,18,1,19,1,19,1,19,5,19,
        297,8,19,10,19,12,19,300,9,19,1,19,1,19,1,19,5,19,305,8,19,10,19,
        12,19,308,9,19,1,19,5,19,311,8,19,10,19,12,19,314,9,19,1,19,3,19,
        317,8,19,3,19,319,8,19,1,19,5,19,322,8,19,10,19,12,19,325,9,19,1,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,5,21,336,8,21,10,21,12,
        21,339,9,21,1,21,1,21,1,21,5,21,344,8,21,10,21,12,21,347,9,21,1,
        21,5,21,350,8,21,10,21,12,21,353,9,21,1,21,3,21,356,8,21,3,21,358,
        8,21,1,21,5,21,361,8,21,10,21,12,21,364,9,21,1,21,1,21,1,22,1,22,
        5,22,370,8,22,10,22,12,22,373,9,22,1,22,1,22,1,22,5,22,378,8,22,
        10,22,12,22,381,9,22,1,22,5,22,384,8,22,10,22,12,22,387,9,22,1,22,
        3,22,390,8,22,3,22,392,8,22,1,22,5,22,395,8,22,10,22,12,22,398,9,
        22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,3,24,409,8,24,1,
        24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,421,8,25,10,
        25,12,25,424,9,25,1,26,1,26,1,26,1,26,3,26,430,8,26,1,26,1,26,1,
        26,1,26,1,26,1,26,4,26,438,8,26,11,26,12,26,439,1,26,1,26,3,26,444,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,4,27,453,8,27,11,27,12,27,
        454,1,27,1,27,1,27,3,27,460,8,27,1,28,1,28,1,29,1,29,1,30,1,30,1,
        30,3,30,469,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,33,1,33,3,33,484,8,33,1,33,1,33,3,33,488,8,33,1,33,1,33,
        3,33,492,8,33,1,33,3,33,495,8,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,3,34,504,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,5,35,513,8,35,
        10,35,12,35,516,9,35,1,35,1,35,3,35,520,8,35,1,36,1,36,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,3,37,537,
        8,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,5,37,
        563,8,37,10,37,12,37,566,9,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,
        1,39,1,39,1,40,1,40,1,40,5,40,580,8,40,10,40,12,40,583,9,40,1,40,
        3,40,586,8,40,3,40,588,8,40,1,40,0,1,74,41,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,0,5,1,0,33,38,1,0,46,47,1,0,43,45,
        1,0,54,55,1,0,48,53,647,0,82,1,0,0,0,2,89,1,0,0,0,4,92,1,0,0,0,6,
        97,1,0,0,0,8,99,1,0,0,0,10,111,1,0,0,0,12,123,1,0,0,0,14,125,1,0,
        0,0,16,128,1,0,0,0,18,130,1,0,0,0,20,141,1,0,0,0,22,172,1,0,0,0,
        24,174,1,0,0,0,26,181,1,0,0,0,28,190,1,0,0,0,30,199,1,0,0,0,32,241,
        1,0,0,0,34,257,1,0,0,0,36,259,1,0,0,0,38,293,1,0,0,0,40,329,1,0,
        0,0,42,333,1,0,0,0,44,367,1,0,0,0,46,401,1,0,0,0,48,405,1,0,0,0,
        50,413,1,0,0,0,52,443,1,0,0,0,54,459,1,0,0,0,56,461,1,0,0,0,58,463,
        1,0,0,0,60,468,1,0,0,0,62,470,1,0,0,0,64,474,1,0,0,0,66,494,1,0,
        0,0,68,498,1,0,0,0,70,505,1,0,0,0,72,521,1,0,0,0,74,536,1,0,0,0,
        76,567,1,0,0,0,78,572,1,0,0,0,80,587,1,0,0,0,82,83,3,2,1,0,83,84,
        5,0,0,1,84,1,1,0,0,0,85,88,3,4,2,0,86,88,5,59,0,0,87,85,1,0,0,0,
        87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,3,1,0,
        0,0,91,89,1,0,0,0,92,93,3,6,3,0,93,5,1,0,0,0,94,98,3,20,10,0,95,
        98,3,52,26,0,96,98,3,30,15,0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,
        0,0,0,98,7,1,0,0,0,99,105,5,25,0,0,100,101,3,10,5,0,101,102,5,59,
        0,0,102,104,1,0,0,0,103,100,1,0,0,0,104,107,1,0,0,0,105,103,1,0,
        0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,109,5,26,
        0,0,109,9,1,0,0,0,110,112,3,12,6,0,111,110,1,0,0,0,111,112,1,0,0,
        0,112,11,1,0,0,0,113,124,3,20,10,0,114,124,3,54,27,0,115,124,3,76,
        38,0,116,124,3,52,26,0,117,124,3,60,30,0,118,124,3,70,35,0,119,124,
        3,16,8,0,120,124,3,18,9,0,121,124,3,14,7,0,122,124,3,74,37,0,123,
        113,1,0,0,0,123,114,1,0,0,0,123,115,1,0,0,0,123,116,1,0,0,0,123,
        117,1,0,0,0,123,118,1,0,0,0,123,119,1,0,0,0,123,120,1,0,0,0,123,
        121,1,0,0,0,123,122,1,0,0,0,124,13,1,0,0,0,125,126,5,16,0,0,126,
        127,3,74,37,0,127,15,1,0,0,0,128,129,5,14,0,0,129,17,1,0,0,0,130,
        139,5,15,0,0,131,136,3,74,37,0,132,133,5,30,0,0,133,135,3,74,37,
        0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,
        0,137,140,1,0,0,0,138,136,1,0,0,0,139,131,1,0,0,0,139,140,1,0,0,
        0,140,19,1,0,0,0,141,142,3,22,11,0,142,143,5,20,0,0,143,155,5,23,
        0,0,144,149,3,78,39,0,145,146,5,30,0,0,146,148,3,78,39,0,147,145,
        1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,152,154,5,30,0,0,153,152,1,0,0,0,153,154,
        1,0,0,0,154,156,1,0,0,0,155,144,1,0,0,0,155,156,1,0,0,0,156,157,
        1,0,0,0,157,158,5,24,0,0,158,159,3,8,4,0,159,21,1,0,0,0,160,173,
        3,28,14,0,161,173,5,3,0,0,162,163,5,23,0,0,163,166,3,28,14,0,164,
        165,5,30,0,0,165,167,3,28,14,0,166,164,1,0,0,0,167,168,1,0,0,0,168,
        166,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,171,5,24,0,0,171,
        173,1,0,0,0,172,160,1,0,0,0,172,161,1,0,0,0,172,162,1,0,0,0,173,
        23,1,0,0,0,174,175,5,4,0,0,175,176,5,49,0,0,176,177,3,28,14,0,177,
        178,5,30,0,0,178,179,3,28,14,0,179,180,5,48,0,0,180,25,1,0,0,0,181,
        182,5,5,0,0,182,183,5,49,0,0,183,184,3,28,14,0,184,185,5,48,0,0,
        185,27,1,0,0,0,186,191,5,6,0,0,187,191,3,24,12,0,188,191,3,26,13,
        0,189,191,5,20,0,0,190,186,1,0,0,0,190,187,1,0,0,0,190,188,1,0,0,
        0,190,189,1,0,0,0,191,196,1,0,0,0,192,193,5,27,0,0,193,195,5,28,
        0,0,194,192,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,
        0,0,197,29,1,0,0,0,198,196,1,0,0,0,199,200,5,1,0,0,200,210,5,20,
        0,0,201,202,5,2,0,0,202,207,5,20,0,0,203,204,5,30,0,0,204,206,5,
        20,0,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,
        0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,210,201,1,0,0,0,210,211,1,
        0,0,0,211,212,1,0,0,0,212,216,5,25,0,0,213,215,5,59,0,0,214,213,
        1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,237,
        1,0,0,0,218,216,1,0,0,0,219,228,3,32,16,0,220,222,5,59,0,0,221,220,
        1,0,0,0,222,223,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,225,
        1,0,0,0,225,227,3,32,16,0,226,221,1,0,0,0,227,230,1,0,0,0,228,226,
        1,0,0,0,228,229,1,0,0,0,229,234,1,0,0,0,230,228,1,0,0,0,231,233,
        5,59,0,0,232,231,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,
        1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,237,219,1,0,0,0,237,238,
        1,0,0,0,238,239,1,0,0,0,239,240,5,26,0,0,240,31,1,0,0,0,241,243,
        5,20,0,0,242,244,5,29,0,0,243,242,1,0,0,0,243,244,1,0,0,0,244,245,
        1,0,0,0,245,246,5,21,0,0,246,247,3,28,14,0,247,33,1,0,0,0,248,258,
        5,57,0,0,249,258,5,56,0,0,250,258,5,58,0,0,251,258,5,18,0,0,252,
        258,5,19,0,0,253,258,3,36,18,0,254,258,3,38,19,0,255,258,3,42,21,
        0,256,258,3,44,22,0,257,248,1,0,0,0,257,249,1,0,0,0,257,250,1,0,
        0,0,257,251,1,0,0,0,257,252,1,0,0,0,257,253,1,0,0,0,257,254,1,0,
        0,0,257,255,1,0,0,0,257,256,1,0,0,0,258,35,1,0,0,0,259,263,5,27,
        0,0,260,262,5,59,0,0,261,260,1,0,0,0,262,265,1,0,0,0,263,261,1,0,
        0,0,263,264,1,0,0,0,264,283,1,0,0,0,265,263,1,0,0,0,266,277,3,74,
        37,0,267,271,5,30,0,0,268,270,5,59,0,0,269,268,1,0,0,0,270,273,1,
        0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,274,1,0,0,0,273,271,1,
        0,0,0,274,276,3,74,37,0,275,267,1,0,0,0,276,279,1,0,0,0,277,275,
        1,0,0,0,277,278,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,280,282,
        5,30,0,0,281,280,1,0,0,0,281,282,1,0,0,0,282,284,1,0,0,0,283,266,
        1,0,0,0,283,284,1,0,0,0,284,288,1,0,0,0,285,287,5,59,0,0,286,285,
        1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,291,
        1,0,0,0,290,288,1,0,0,0,291,292,5,28,0,0,292,37,1,0,0,0,293,294,
        5,25,0,0,294,298,5,25,0,0,295,297,5,59,0,0,296,295,1,0,0,0,297,300,
        1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,318,1,0,0,0,300,298,
        1,0,0,0,301,312,3,40,20,0,302,306,5,30,0,0,303,305,5,59,0,0,304,
        303,1,0,0,0,305,308,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,
        309,1,0,0,0,308,306,1,0,0,0,309,311,3,40,20,0,310,302,1,0,0,0,311,
        314,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,316,1,0,0,0,314,
        312,1,0,0,0,315,317,5,30,0,0,316,315,1,0,0,0,316,317,1,0,0,0,317,
        319,1,0,0,0,318,301,1,0,0,0,318,319,1,0,0,0,319,323,1,0,0,0,320,
        322,5,59,0,0,321,320,1,0,0,0,322,325,1,0,0,0,323,321,1,0,0,0,323,
        324,1,0,0,0,324,326,1,0,0,0,325,323,1,0,0,0,326,327,5,26,0,0,327,
        328,5,26,0,0,328,39,1,0,0,0,329,330,3,74,37,0,330,331,5,21,0,0,331,
        332,3,74,37,0,332,41,1,0,0,0,333,337,5,32,0,0,334,336,5,59,0,0,335,
        334,1,0,0,0,336,339,1,0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,
        357,1,0,0,0,339,337,1,0,0,0,340,351,3,74,37,0,341,345,5,30,0,0,342,
        344,5,59,0,0,343,342,1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,345,
        346,1,0,0,0,346,348,1,0,0,0,347,345,1,0,0,0,348,350,3,74,37,0,349,
        341,1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,352,
        355,1,0,0,0,353,351,1,0,0,0,354,356,5,30,0,0,355,354,1,0,0,0,355,
        356,1,0,0,0,356,358,1,0,0,0,357,340,1,0,0,0,357,358,1,0,0,0,358,
        362,1,0,0,0,359,361,5,59,0,0,360,359,1,0,0,0,361,364,1,0,0,0,362,
        360,1,0,0,0,362,363,1,0,0,0,363,365,1,0,0,0,364,362,1,0,0,0,365,
        366,5,28,0,0,366,43,1,0,0,0,367,371,5,25,0,0,368,370,5,59,0,0,369,
        368,1,0,0,0,370,373,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,
        391,1,0,0,0,373,371,1,0,0,0,374,385,3,46,23,0,375,379,5,30,0,0,376,
        378,5,59,0,0,377,376,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,
        380,1,0,0,0,380,382,1,0,0,0,381,379,1,0,0,0,382,384,3,46,23,0,383,
        375,1,0,0,0,384,387,1,0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,
        389,1,0,0,0,387,385,1,0,0,0,388,390,5,30,0,0,389,388,1,0,0,0,389,
        390,1,0,0,0,390,392,1,0,0,0,391,374,1,0,0,0,391,392,1,0,0,0,392,
        396,1,0,0,0,393,395,5,59,0,0,394,393,1,0,0,0,395,398,1,0,0,0,396,
        394,1,0,0,0,396,397,1,0,0,0,397,399,1,0,0,0,398,396,1,0,0,0,399,
        400,5,26,0,0,400,45,1,0,0,0,401,402,5,20,0,0,402,403,5,21,0,0,403,
        404,3,74,37,0,404,47,1,0,0,0,405,408,5,20,0,0,406,407,5,21,0,0,407,
        409,3,28,14,0,408,406,1,0,0,0,408,409,1,0,0,0,409,410,1,0,0,0,410,
        411,5,33,0,0,411,412,3,74,37,0,412,49,1,0,0,0,413,422,5,20,0,0,414,
        415,5,27,0,0,415,416,3,74,37,0,416,417,5,28,0,0,417,421,1,0,0,0,
        418,419,5,31,0,0,419,421,3,50,25,0,420,414,1,0,0,0,420,418,1,0,0,
        0,421,424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,51,1,0,0,0,
        424,422,1,0,0,0,425,426,5,17,0,0,426,429,5,20,0,0,427,428,5,21,0,
        0,428,430,3,28,14,0,429,427,1,0,0,0,429,430,1,0,0,0,430,431,1,0,
        0,0,431,432,5,33,0,0,432,444,3,74,37,0,433,434,5,17,0,0,434,437,
        5,20,0,0,435,436,5,30,0,0,436,438,5,20,0,0,437,435,1,0,0,0,438,439,
        1,0,0,0,439,437,1,0,0,0,439,440,1,0,0,0,440,441,1,0,0,0,441,442,
        5,33,0,0,442,444,3,76,38,0,443,425,1,0,0,0,443,433,1,0,0,0,444,53,
        1,0,0,0,445,446,3,50,25,0,446,447,7,0,0,0,447,448,3,74,37,0,448,
        460,1,0,0,0,449,452,3,50,25,0,450,451,5,30,0,0,451,453,3,50,25,0,
        452,450,1,0,0,0,453,454,1,0,0,0,454,452,1,0,0,0,454,455,1,0,0,0,
        455,456,1,0,0,0,456,457,5,33,0,0,457,458,3,76,38,0,458,460,1,0,0,
        0,459,445,1,0,0,0,459,449,1,0,0,0,460,55,1,0,0,0,461,462,3,8,4,0,
        462,57,1,0,0,0,463,464,3,8,4,0,464,59,1,0,0,0,465,469,3,66,33,0,
        466,469,3,62,31,0,467,469,3,64,32,0,468,465,1,0,0,0,468,466,1,0,
        0,0,468,467,1,0,0,0,469,61,1,0,0,0,470,471,5,12,0,0,471,472,3,72,
        36,0,472,473,3,58,29,0,473,63,1,0,0,0,474,475,5,13,0,0,475,476,3,
        58,29,0,476,477,5,12,0,0,477,478,5,23,0,0,478,479,3,72,36,0,479,
        480,5,24,0,0,480,65,1,0,0,0,481,483,5,10,0,0,482,484,3,48,24,0,483,
        482,1,0,0,0,483,484,1,0,0,0,484,485,1,0,0,0,485,487,5,22,0,0,486,
        488,3,72,36,0,487,486,1,0,0,0,487,488,1,0,0,0,488,489,1,0,0,0,489,
        491,5,22,0,0,490,492,3,74,37,0,491,490,1,0,0,0,491,492,1,0,0,0,492,
        495,1,0,0,0,493,495,3,68,34,0,494,481,1,0,0,0,494,493,1,0,0,0,495,
        496,1,0,0,0,496,497,3,58,29,0,497,67,1,0,0,0,498,499,5,10,0,0,499,
        500,5,20,0,0,500,503,5,11,0,0,501,504,3,76,38,0,502,504,3,50,25,
        0,503,501,1,0,0,0,503,502,1,0,0,0,504,69,1,0,0,0,505,506,5,7,0,0,
        506,507,3,72,36,0,507,514,3,56,28,0,508,509,5,8,0,0,509,510,3,72,
        36,0,510,511,3,56,28,0,511,513,1,0,0,0,512,508,1,0,0,0,513,516,1,
        0,0,0,514,512,1,0,0,0,514,515,1,0,0,0,515,519,1,0,0,0,516,514,1,
        0,0,0,517,518,5,9,0,0,518,520,3,56,28,0,519,517,1,0,0,0,519,520,
        1,0,0,0,520,71,1,0,0,0,521,522,3,74,37,0,522,73,1,0,0,0,523,524,
        6,37,-1,0,524,525,5,23,0,0,525,526,3,74,37,0,526,527,5,24,0,0,527,
        537,1,0,0,0,528,537,3,34,17,0,529,537,3,76,38,0,530,537,3,50,25,
        0,531,532,3,50,25,0,532,533,7,1,0,0,533,537,1,0,0,0,534,535,5,41,
        0,0,535,537,3,74,37,8,536,523,1,0,0,0,536,528,1,0,0,0,536,529,1,
        0,0,0,536,530,1,0,0,0,536,531,1,0,0,0,536,534,1,0,0,0,537,564,1,
        0,0,0,538,539,10,7,0,0,539,540,5,42,0,0,540,563,3,74,37,7,541,542,
        10,6,0,0,542,543,7,2,0,0,543,563,3,74,37,7,544,545,10,5,0,0,545,
        546,7,3,0,0,546,563,3,74,37,6,547,548,10,4,0,0,548,549,7,4,0,0,549,
        563,3,74,37,5,550,551,10,3,0,0,551,552,5,39,0,0,552,563,3,74,37,
        4,553,554,10,2,0,0,554,555,5,40,0,0,555,563,3,74,37,3,556,557,10,
        1,0,0,557,558,5,29,0,0,558,559,3,74,37,0,559,560,5,21,0,0,560,561,
        3,74,37,2,561,563,1,0,0,0,562,538,1,0,0,0,562,541,1,0,0,0,562,544,
        1,0,0,0,562,547,1,0,0,0,562,550,1,0,0,0,562,553,1,0,0,0,562,556,
        1,0,0,0,563,566,1,0,0,0,564,562,1,0,0,0,564,565,1,0,0,0,565,75,1,
        0,0,0,566,564,1,0,0,0,567,568,5,20,0,0,568,569,5,23,0,0,569,570,
        3,80,40,0,570,571,5,24,0,0,571,77,1,0,0,0,572,573,5,20,0,0,573,574,
        5,21,0,0,574,575,3,28,14,0,575,79,1,0,0,0,576,581,3,74,37,0,577,
        578,5,30,0,0,578,580,3,74,37,0,579,577,1,0,0,0,580,583,1,0,0,0,581,
        579,1,0,0,0,581,582,1,0,0,0,582,585,1,0,0,0,583,581,1,0,0,0,584,
        586,5,30,0,0,585,584,1,0,0,0,585,586,1,0,0,0,586,588,1,0,0,0,587,
        576,1,0,0,0,587,588,1,0,0,0,588,81,1,0,0,0,70,87,89,97,105,111,123,
        136,139,149,153,155,168,172,190,196,207,210,216,223,228,234,237,
        243,257,263,271,277,281,283,288,298,306,312,316,318,323,337,345,
        351,355,357,362,371,379,385,389,391,396,408,420,422,429,439,443,
        454,459,468,483,487,491,494,503,514,519,536,562,564,581,585,587
    ]

class SwagLangParser ( Parser ):

    grammarFileName = "SwagLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'interface'", "'extends'", "'void'", 
                     "'map'", "'set'", "<INVALID>", "'if'", "<INVALID>", 
                     "'else'", "'for'", "'in'", "'while'", "'do'", "'break'", 
                     "'return'", "'defer'", "<INVALID>", "<INVALID>", "'null'", 
                     "<INVALID>", "':'", "';'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'?'", "','", "'.'", "'#['", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'&&'", "'||'", "'!'", 
                     "'**'", "'*'", "'/'", "'%'", "'++'", "'--'", "'>'", 
                     "'<'", "'=='", "'!='", "'>='", "'<='", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INTERFACE", "EXTENDS", "VOID", "MAP", 
                      "SET", "TYPE", "IF", "ELSE_IF", "ELSE", "FOR", "IN", 
                      "WHILE", "DO", "BREAK", "RETURN", "DEFER", "ACCESS_MOD", 
                      "BOOL", "NULL", "IDENT", "COLUMN", "SEMICOL", "L_PAREN", 
                      "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", 
                      "QUESTION", "COMMA", "DOT", "SET_START", "ASSIGN", 
                      "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "AND", "OR", "NOT", "EXP", "MUL", "DIV", 
                      "MOD", "INC", "DEC", "GT", "LT", "EQ", "NEQ", "GTE", 
                      "LTE", "PLUS", "MINUS", "STRING", "INT", "FLOAT", 
                      "NWLN", "SPACE", "COMMENT", "INLINE_COMMENT" ]

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
    RULE_map_type = 12
    RULE_set_type = 13
    RULE_type_ann = 14
    RULE_interface_decl = 15
    RULE_interface_field = 16
    RULE_data = 17
    RULE_array = 18
    RULE_map = 19
    RULE_map_field = 20
    RULE_set = 21
    RULE_struct = 22
    RULE_struct_field = 23
    RULE_no_acs_mode_var_decl = 24
    RULE_var_ref = 25
    RULE_var_decl = 26
    RULE_var_assign = 27
    RULE_conditional_body = 28
    RULE_loop_body = 29
    RULE_loop = 30
    RULE_while_loop = 31
    RULE_do_while_loop = 32
    RULE_for_loop = 33
    RULE_forin = 34
    RULE_conditional = 35
    RULE_condition = 36
    RULE_expr = 37
    RULE_func_call = 38
    RULE_param_decl = 39
    RULE_params = 40

    ruleNames =  [ "prog", "stmts", "stmt", "pure_stmt", "code_block", "func_stmt", 
                   "pure_func_stmt", "defer", "break", "return", "func_decl", 
                   "return_type", "map_type", "set_type", "type_ann", "interface_decl", 
                   "interface_field", "data", "array", "map", "map_field", 
                   "set", "struct", "struct_field", "no_acs_mode_var_decl", 
                   "var_ref", "var_decl", "var_assign", "conditional_body", 
                   "loop_body", "loop", "while_loop", "do_while_loop", "for_loop", 
                   "forin", "conditional", "condition", "expr", "func_call", 
                   "param_decl", "params" ]

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
    RETURN=15
    DEFER=16
    ACCESS_MOD=17
    BOOL=18
    NULL=19
    IDENT=20
    COLUMN=21
    SEMICOL=22
    L_PAREN=23
    R_PAREN=24
    L_CURLY=25
    R_CURLY=26
    L_BRACKET=27
    R_BRACKET=28
    QUESTION=29
    COMMA=30
    DOT=31
    SET_START=32
    ASSIGN=33
    ADD_ASSIGN=34
    SUB_ASSIGN=35
    MUL_ASSIGN=36
    DIV_ASSIGN=37
    MOD_ASSIGN=38
    AND=39
    OR=40
    NOT=41
    EXP=42
    MUL=43
    DIV=44
    MOD=45
    INC=46
    DEC=47
    GT=48
    LT=49
    EQ=50
    NEQ=51
    GTE=52
    LTE=53
    PLUS=54
    MINUS=55
    STRING=56
    INT=57
    FLOAT=58
    NWLN=59
    SPACE=60
    COMMENT=61
    INLINE_COMMENT=62

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
            self.state = 82
            self.stmts()
            self.state = 83
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
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752312991866) != 0):
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 4, 5, 6, 17, 20, 23]:
                    self.state = 85
                    self.stmt()
                    pass
                elif token in [59]:
                    self.state = 86
                    self.match(SwagLangParser.NWLN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 91
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
            self.state = 92
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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 20, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.func_decl()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.var_decl()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
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
            self.state = 99
            self.match(SwagLangParser.L_CURLY)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1080866114065396984) != 0):
                self.state = 100
                self.func_stmt()
                self.state = 101
                self.match(SwagLangParser.NWLN)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
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
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504405361761973496) != 0):
                self.state = 110
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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.var_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.var_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                self.loop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 118
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 119
                self.break_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 120
                self.return_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 121
                self.defer()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 122
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
            self.state = 125
            self.match(SwagLangParser.DEFER)
            self.state = 126
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
            self.state = 128
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
            self.state = 130
            self.match(SwagLangParser.RETURN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504405361761714176) != 0):
                self.state = 131
                self.expr(0)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 132
                    self.match(SwagLangParser.COMMA)
                    self.state = 133
                    self.expr(0)
                    self.state = 138
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
            self.state = 141
            self.return_type()
            self.state = 142
            self.match(SwagLangParser.IDENT)
            self.state = 143
            self.match(SwagLangParser.L_PAREN)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 144
                self.param_decl()
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 145
                        self.match(SwagLangParser.COMMA)
                        self.state = 146
                        self.param_decl() 
                    self.state = 151
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 152
                    self.match(SwagLangParser.COMMA)




            self.state = 157
            self.match(SwagLangParser.R_PAREN)
            self.state = 158
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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.type_ann()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(SwagLangParser.VOID)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(SwagLangParser.L_PAREN)
                self.state = 163
                self.type_ann()
                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 164
                    self.match(SwagLangParser.COMMA)
                    self.state = 165
                    self.type_ann()
                    self.state = 168 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                self.state = 170
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
        self.enterRule(localctx, 24, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(SwagLangParser.MAP)
            self.state = 175
            self.match(SwagLangParser.LT)
            self.state = 176
            self.type_ann()
            self.state = 177
            self.match(SwagLangParser.COMMA)
            self.state = 178
            self.type_ann()
            self.state = 179
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
        self.enterRule(localctx, 26, self.RULE_set_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(SwagLangParser.SET)
            self.state = 182
            self.match(SwagLangParser.LT)
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
        self.enterRule(localctx, 28, self.RULE_type_ann)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 186
                self.match(SwagLangParser.TYPE)
                pass
            elif token in [4]:
                self.state = 187
                self.map_type()
                pass
            elif token in [5]:
                self.state = 188
                self.set_type()
                pass
            elif token in [20]:
                self.state = 189
                self.match(SwagLangParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 192
                self.match(SwagLangParser.L_BRACKET)
                self.state = 193
                self.match(SwagLangParser.R_BRACKET)
                self.state = 198
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
        self.enterRule(localctx, 30, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(SwagLangParser.INTERFACE)
            self.state = 200
            self.match(SwagLangParser.IDENT)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 201
                self.match(SwagLangParser.EXTENDS)
                self.state = 202
                self.match(SwagLangParser.IDENT)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 203
                    self.match(SwagLangParser.COMMA)
                    self.state = 204
                    self.match(SwagLangParser.IDENT)
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 212
            self.match(SwagLangParser.L_CURLY)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 213
                self.match(SwagLangParser.NWLN)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 219
                self.interface_field()
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 221 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 220
                            self.match(SwagLangParser.NWLN)
                            self.state = 223 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==59):
                                break

                        self.state = 225
                        self.interface_field() 
                    self.state = 230
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==59:
                    self.state = 231
                    self.match(SwagLangParser.NWLN)
                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 239
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
        self.enterRule(localctx, 32, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(SwagLangParser.IDENT)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 242
                self.match(SwagLangParser.QUESTION)


            self.state = 245
            self.match(SwagLangParser.COLUMN)
            self.state = 246
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
        self.enterRule(localctx, 34, self.RULE_data)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(SwagLangParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(SwagLangParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.match(SwagLangParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.match(SwagLangParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.match(SwagLangParser.NULL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 254
                self.map_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 255
                self.set_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 256
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
        self.enterRule(localctx, 36, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(SwagLangParser.L_BRACKET)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self.match(SwagLangParser.NWLN) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504405361761714176) != 0):
                self.state = 266
                self.expr(0)
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 267
                        self.match(SwagLangParser.COMMA)
                        self.state = 271
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==59:
                            self.state = 268
                            self.match(SwagLangParser.NWLN)
                            self.state = 273
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 274
                        self.expr(0) 
                    self.state = 279
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 280
                    self.match(SwagLangParser.COMMA)




            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 285
                self.match(SwagLangParser.NWLN)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
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
        self.enterRule(localctx, 38, self.RULE_map)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(SwagLangParser.L_CURLY)
            self.state = 294
            self.match(SwagLangParser.L_CURLY)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 295
                    self.match(SwagLangParser.NWLN) 
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504405361761714176) != 0):
                self.state = 301
                self.map_field()
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 302
                        self.match(SwagLangParser.COMMA)
                        self.state = 306
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==59:
                            self.state = 303
                            self.match(SwagLangParser.NWLN)
                            self.state = 308
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 309
                        self.map_field() 
                    self.state = 314
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 315
                    self.match(SwagLangParser.COMMA)




            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 320
                self.match(SwagLangParser.NWLN)
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 326
            self.match(SwagLangParser.R_CURLY)
            self.state = 327
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
        self.enterRule(localctx, 40, self.RULE_map_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.expr(0)
            self.state = 330
            self.match(SwagLangParser.COLUMN)
            self.state = 331
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
        self.enterRule(localctx, 42, self.RULE_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(SwagLangParser.SET_START)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 334
                    self.match(SwagLangParser.NWLN) 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504405361761714176) != 0):
                self.state = 340
                self.expr(0)
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 341
                        self.match(SwagLangParser.COMMA)
                        self.state = 345
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==59:
                            self.state = 342
                            self.match(SwagLangParser.NWLN)
                            self.state = 347
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 348
                        self.expr(0) 
                    self.state = 353
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 354
                    self.match(SwagLangParser.COMMA)




            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 359
                self.match(SwagLangParser.NWLN)
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
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
        self.enterRule(localctx, 44, self.RULE_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(SwagLangParser.L_CURLY)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 368
                    self.match(SwagLangParser.NWLN) 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 374
                self.struct_field()
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 375
                        self.match(SwagLangParser.COMMA)
                        self.state = 379
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==59:
                            self.state = 376
                            self.match(SwagLangParser.NWLN)
                            self.state = 381
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 382
                        self.struct_field() 
                    self.state = 387
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 388
                    self.match(SwagLangParser.COMMA)




            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 393
                self.match(SwagLangParser.NWLN)
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 399
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
        self.enterRule(localctx, 46, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(SwagLangParser.IDENT)
            self.state = 402
            self.match(SwagLangParser.COLUMN)
            self.state = 403
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
        self.enterRule(localctx, 48, self.RULE_no_acs_mode_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(SwagLangParser.IDENT)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 406
                self.match(SwagLangParser.COLUMN)
                self.state = 407
                self.type_ann()


            self.state = 410
            self.match(SwagLangParser.ASSIGN)
            self.state = 411
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
        self.enterRule(localctx, 50, self.RULE_var_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(SwagLangParser.IDENT)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 420
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [27]:
                        self.state = 414
                        self.match(SwagLangParser.L_BRACKET)
                        self.state = 415
                        self.expr(0)
                        self.state = 416
                        self.match(SwagLangParser.R_BRACKET)
                        pass
                    elif token in [31]:
                        self.state = 418
                        self.match(SwagLangParser.DOT)
                        self.state = 419
                        self.var_ref()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 424
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
        self.enterRule(localctx, 52, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 426
                self.match(SwagLangParser.IDENT)
                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 427
                    self.match(SwagLangParser.COLUMN)
                    self.state = 428
                    self.type_ann()


                self.state = 431
                self.match(SwagLangParser.ASSIGN)
                self.state = 432
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 434
                self.match(SwagLangParser.IDENT)
                self.state = 437 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 435
                    self.match(SwagLangParser.COMMA)
                    self.state = 436
                    self.match(SwagLangParser.IDENT)
                    self.state = 439 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                self.state = 441
                self.match(SwagLangParser.ASSIGN)
                self.state = 442
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
        self.enterRule(localctx, 54, self.RULE_var_assign)
        self._la = 0 # Token type
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.var_ref()
                self.state = 446
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 541165879296) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 447
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.var_ref()
                self.state = 452 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 450
                    self.match(SwagLangParser.COMMA)
                    self.state = 451
                    self.var_ref()
                    self.state = 454 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                self.state = 456
                self.match(SwagLangParser.ASSIGN)
                self.state = 457
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
        self.enterRule(localctx, 56, self.RULE_conditional_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
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
        self.enterRule(localctx, 58, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
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
        self.enterRule(localctx, 60, self.RULE_loop)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.for_loop()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.while_loop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
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
        self.enterRule(localctx, 62, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(SwagLangParser.WHILE)
            self.state = 471
            self.condition()
            self.state = 472
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
        self.enterRule(localctx, 64, self.RULE_do_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(SwagLangParser.DO)
            self.state = 475
            self.loop_body()
            self.state = 476
            self.match(SwagLangParser.WHILE)
            self.state = 477
            self.match(SwagLangParser.L_PAREN)
            self.state = 478
            self.condition()
            self.state = 479
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
        self.enterRule(localctx, 66, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 481
                self.match(SwagLangParser.FOR)

                self.state = 483
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 482
                    self.no_acs_mode_var_decl()


                self.state = 485
                self.match(SwagLangParser.SEMICOL)
                self.state = 487
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504405361761714176) != 0):
                    self.state = 486
                    self.condition()


                self.state = 489
                self.match(SwagLangParser.SEMICOL)
                self.state = 491
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 490
                    self.expr(0)


                pass

            elif la_ == 2:
                self.state = 493
                self.forin()
                pass


            self.state = 496
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
        self.enterRule(localctx, 68, self.RULE_forin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(SwagLangParser.FOR)
            self.state = 499
            self.match(SwagLangParser.IDENT)
            self.state = 500
            self.match(SwagLangParser.IN)
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 501
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 502
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
        self.enterRule(localctx, 70, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(SwagLangParser.IF)
            self.state = 506
            self.condition()
            self.state = 507
            self.conditional_body()
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 508
                self.match(SwagLangParser.ELSE_IF)
                self.state = 509
                self.condition()
                self.state = 510
                self.conditional_body()
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 517
                self.match(SwagLangParser.ELSE)
                self.state = 518
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
        self.enterRule(localctx, 72, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 524
                self.match(SwagLangParser.L_PAREN)
                self.state = 525
                self.expr(0)
                self.state = 526
                self.match(SwagLangParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 528
                self.data()
                pass

            elif la_ == 3:
                self.state = 529
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 530
                self.var_ref()
                pass

            elif la_ == 5:
                self.state = 531
                self.var_ref()
                self.state = 532
                _la = self._input.LA(1)
                if not(_la==46 or _la==47):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.state = 534
                self.match(SwagLangParser.NOT)
                self.state = 535
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 564
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 562
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 538
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 539
                        self.match(SwagLangParser.EXP)
                        self.state = 540
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 541
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 542
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61572651155456) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 543
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 544
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 545
                        _la = self._input.LA(1)
                        if not(_la==54 or _la==55):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 546
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 547
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 548
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17732923532771328) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 549
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 550
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 551
                        self.match(SwagLangParser.AND)
                        self.state = 552
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 553
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 554
                        self.match(SwagLangParser.OR)
                        self.state = 555
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 556
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 557
                        self.match(SwagLangParser.QUESTION)
                        self.state = 558
                        self.expr(0)
                        self.state = 559
                        self.match(SwagLangParser.COLUMN)
                        self.state = 560
                        self.expr(2)
                        pass

             
                self.state = 566
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
        self.enterRule(localctx, 76, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(SwagLangParser.IDENT)
            self.state = 568
            self.match(SwagLangParser.L_PAREN)
            self.state = 569
            self.params()
            self.state = 570
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
        self.enterRule(localctx, 78, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(SwagLangParser.IDENT)
            self.state = 573
            self.match(SwagLangParser.COLUMN)
            self.state = 574
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
        self.enterRule(localctx, 80, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504405361761714176) != 0):
                self.state = 576
                self.expr(0)
                self.state = 581
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 577
                        self.match(SwagLangParser.COMMA)
                        self.state = 578
                        self.expr(0) 
                    self.state = 583
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

                self.state = 585
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 584
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
        self._predicates[37] = self.expr_sempred
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
         




