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
        4,1,61,589,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        3,17,257,8,17,1,18,1,18,5,18,261,8,18,10,18,12,18,264,9,18,1,18,
        1,18,1,18,5,18,269,8,18,10,18,12,18,272,9,18,1,18,5,18,275,8,18,
        10,18,12,18,278,9,18,1,18,3,18,281,8,18,3,18,283,8,18,1,18,5,18,
        286,8,18,10,18,12,18,289,9,18,1,18,1,18,1,19,1,19,1,19,5,19,296,
        8,19,10,19,12,19,299,9,19,1,19,1,19,1,19,5,19,304,8,19,10,19,12,
        19,307,9,19,1,19,5,19,310,8,19,10,19,12,19,313,9,19,1,19,3,19,316,
        8,19,3,19,318,8,19,1,19,5,19,321,8,19,10,19,12,19,324,9,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,5,21,335,8,21,10,21,12,21,
        338,9,21,1,21,1,21,1,21,5,21,343,8,21,10,21,12,21,346,9,21,1,21,
        5,21,349,8,21,10,21,12,21,352,9,21,1,21,3,21,355,8,21,3,21,357,8,
        21,1,21,5,21,360,8,21,10,21,12,21,363,9,21,1,21,1,21,1,22,1,22,5,
        22,369,8,22,10,22,12,22,372,9,22,1,22,1,22,1,22,5,22,377,8,22,10,
        22,12,22,380,9,22,1,22,5,22,383,8,22,10,22,12,22,386,9,22,1,22,3,
        22,389,8,22,3,22,391,8,22,1,22,5,22,394,8,22,10,22,12,22,397,9,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,3,24,408,8,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,420,8,25,10,25,
        12,25,423,9,25,1,26,1,26,1,26,1,26,3,26,429,8,26,1,26,1,26,1,26,
        1,26,1,26,1,26,4,26,437,8,26,11,26,12,26,438,1,26,1,26,3,26,443,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,4,27,452,8,27,11,27,12,27,
        453,1,27,1,27,1,27,3,27,459,8,27,1,28,1,28,1,29,1,29,1,30,1,30,1,
        30,3,30,468,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,33,1,33,3,33,483,8,33,1,33,1,33,3,33,487,8,33,1,33,1,33,
        3,33,491,8,33,1,33,3,33,494,8,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,3,34,503,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,5,35,512,8,35,
        10,35,12,35,515,9,35,1,35,1,35,3,35,519,8,35,1,36,1,36,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,3,37,536,
        8,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,5,37,
        562,8,37,10,37,12,37,565,9,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,
        1,39,1,39,1,40,1,40,1,40,5,40,579,8,40,10,40,12,40,582,9,40,1,40,
        3,40,585,8,40,3,40,587,8,40,1,40,0,1,74,41,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,0,5,1,0,32,37,1,0,45,46,1,0,42,44,
        1,0,53,54,1,0,47,52,645,0,82,1,0,0,0,2,89,1,0,0,0,4,92,1,0,0,0,6,
        97,1,0,0,0,8,99,1,0,0,0,10,111,1,0,0,0,12,123,1,0,0,0,14,125,1,0,
        0,0,16,128,1,0,0,0,18,130,1,0,0,0,20,141,1,0,0,0,22,172,1,0,0,0,
        24,174,1,0,0,0,26,181,1,0,0,0,28,190,1,0,0,0,30,199,1,0,0,0,32,241,
        1,0,0,0,34,256,1,0,0,0,36,258,1,0,0,0,38,292,1,0,0,0,40,328,1,0,
        0,0,42,332,1,0,0,0,44,366,1,0,0,0,46,400,1,0,0,0,48,404,1,0,0,0,
        50,412,1,0,0,0,52,442,1,0,0,0,54,458,1,0,0,0,56,460,1,0,0,0,58,462,
        1,0,0,0,60,467,1,0,0,0,62,469,1,0,0,0,64,473,1,0,0,0,66,493,1,0,
        0,0,68,497,1,0,0,0,70,504,1,0,0,0,72,520,1,0,0,0,74,535,1,0,0,0,
        76,566,1,0,0,0,78,571,1,0,0,0,80,586,1,0,0,0,82,83,3,2,1,0,83,84,
        5,0,0,1,84,1,1,0,0,0,85,88,3,4,2,0,86,88,5,58,0,0,87,85,1,0,0,0,
        87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,3,1,0,
        0,0,91,89,1,0,0,0,92,93,3,6,3,0,93,5,1,0,0,0,94,98,3,20,10,0,95,
        98,3,52,26,0,96,98,3,30,15,0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,
        0,0,0,98,7,1,0,0,0,99,105,5,24,0,0,100,101,3,10,5,0,101,102,5,58,
        0,0,102,104,1,0,0,0,103,100,1,0,0,0,104,107,1,0,0,0,105,103,1,0,
        0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,109,5,25,
        0,0,109,9,1,0,0,0,110,112,3,12,6,0,111,110,1,0,0,0,111,112,1,0,0,
        0,112,11,1,0,0,0,113,124,3,20,10,0,114,124,3,54,27,0,115,124,3,76,
        38,0,116,124,3,52,26,0,117,124,3,60,30,0,118,124,3,70,35,0,119,124,
        3,16,8,0,120,124,3,18,9,0,121,124,3,14,7,0,122,124,3,74,37,0,123,
        113,1,0,0,0,123,114,1,0,0,0,123,115,1,0,0,0,123,116,1,0,0,0,123,
        117,1,0,0,0,123,118,1,0,0,0,123,119,1,0,0,0,123,120,1,0,0,0,123,
        121,1,0,0,0,123,122,1,0,0,0,124,13,1,0,0,0,125,126,5,16,0,0,126,
        127,3,74,37,0,127,15,1,0,0,0,128,129,5,14,0,0,129,17,1,0,0,0,130,
        139,5,15,0,0,131,136,3,74,37,0,132,133,5,29,0,0,133,135,3,74,37,
        0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,
        0,137,140,1,0,0,0,138,136,1,0,0,0,139,131,1,0,0,0,139,140,1,0,0,
        0,140,19,1,0,0,0,141,142,3,22,11,0,142,143,5,19,0,0,143,155,5,22,
        0,0,144,149,3,78,39,0,145,146,5,29,0,0,146,148,3,78,39,0,147,145,
        1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,152,154,5,29,0,0,153,152,1,0,0,0,153,154,
        1,0,0,0,154,156,1,0,0,0,155,144,1,0,0,0,155,156,1,0,0,0,156,157,
        1,0,0,0,157,158,5,23,0,0,158,159,3,8,4,0,159,21,1,0,0,0,160,173,
        3,28,14,0,161,173,5,3,0,0,162,163,5,22,0,0,163,166,3,28,14,0,164,
        165,5,29,0,0,165,167,3,28,14,0,166,164,1,0,0,0,167,168,1,0,0,0,168,
        166,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,171,5,23,0,0,171,
        173,1,0,0,0,172,160,1,0,0,0,172,161,1,0,0,0,172,162,1,0,0,0,173,
        23,1,0,0,0,174,175,5,4,0,0,175,176,5,48,0,0,176,177,3,28,14,0,177,
        178,5,29,0,0,178,179,3,28,14,0,179,180,5,47,0,0,180,25,1,0,0,0,181,
        182,5,5,0,0,182,183,5,48,0,0,183,184,3,28,14,0,184,185,5,47,0,0,
        185,27,1,0,0,0,186,191,5,6,0,0,187,191,3,24,12,0,188,191,3,26,13,
        0,189,191,5,19,0,0,190,186,1,0,0,0,190,187,1,0,0,0,190,188,1,0,0,
        0,190,189,1,0,0,0,191,196,1,0,0,0,192,193,5,26,0,0,193,195,5,27,
        0,0,194,192,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,
        0,0,197,29,1,0,0,0,198,196,1,0,0,0,199,200,5,1,0,0,200,210,5,19,
        0,0,201,202,5,2,0,0,202,207,5,19,0,0,203,204,5,29,0,0,204,206,5,
        19,0,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,
        0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,210,201,1,0,0,0,210,211,1,
        0,0,0,211,212,1,0,0,0,212,216,5,24,0,0,213,215,5,58,0,0,214,213,
        1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,237,
        1,0,0,0,218,216,1,0,0,0,219,228,3,32,16,0,220,222,5,58,0,0,221,220,
        1,0,0,0,222,223,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,225,
        1,0,0,0,225,227,3,32,16,0,226,221,1,0,0,0,227,230,1,0,0,0,228,226,
        1,0,0,0,228,229,1,0,0,0,229,234,1,0,0,0,230,228,1,0,0,0,231,233,
        5,58,0,0,232,231,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,
        1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,237,219,1,0,0,0,237,238,
        1,0,0,0,238,239,1,0,0,0,239,240,5,25,0,0,240,31,1,0,0,0,241,243,
        5,19,0,0,242,244,5,28,0,0,243,242,1,0,0,0,243,244,1,0,0,0,244,245,
        1,0,0,0,245,246,5,20,0,0,246,247,3,28,14,0,247,33,1,0,0,0,248,257,
        5,56,0,0,249,257,5,55,0,0,250,257,5,57,0,0,251,257,5,18,0,0,252,
        257,3,36,18,0,253,257,3,38,19,0,254,257,3,42,21,0,255,257,3,44,22,
        0,256,248,1,0,0,0,256,249,1,0,0,0,256,250,1,0,0,0,256,251,1,0,0,
        0,256,252,1,0,0,0,256,253,1,0,0,0,256,254,1,0,0,0,256,255,1,0,0,
        0,257,35,1,0,0,0,258,262,5,26,0,0,259,261,5,58,0,0,260,259,1,0,0,
        0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,282,1,0,0,
        0,264,262,1,0,0,0,265,276,3,74,37,0,266,270,5,29,0,0,267,269,5,58,
        0,0,268,267,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,
        0,0,271,273,1,0,0,0,272,270,1,0,0,0,273,275,3,74,37,0,274,266,1,
        0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,280,1,
        0,0,0,278,276,1,0,0,0,279,281,5,29,0,0,280,279,1,0,0,0,280,281,1,
        0,0,0,281,283,1,0,0,0,282,265,1,0,0,0,282,283,1,0,0,0,283,287,1,
        0,0,0,284,286,5,58,0,0,285,284,1,0,0,0,286,289,1,0,0,0,287,285,1,
        0,0,0,287,288,1,0,0,0,288,290,1,0,0,0,289,287,1,0,0,0,290,291,5,
        27,0,0,291,37,1,0,0,0,292,293,5,24,0,0,293,297,5,24,0,0,294,296,
        5,58,0,0,295,294,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,298,
        1,0,0,0,298,317,1,0,0,0,299,297,1,0,0,0,300,311,3,40,20,0,301,305,
        5,29,0,0,302,304,5,58,0,0,303,302,1,0,0,0,304,307,1,0,0,0,305,303,
        1,0,0,0,305,306,1,0,0,0,306,308,1,0,0,0,307,305,1,0,0,0,308,310,
        3,40,20,0,309,301,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,
        1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,314,316,5,29,0,0,315,314,
        1,0,0,0,315,316,1,0,0,0,316,318,1,0,0,0,317,300,1,0,0,0,317,318,
        1,0,0,0,318,322,1,0,0,0,319,321,5,58,0,0,320,319,1,0,0,0,321,324,
        1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,325,1,0,0,0,324,322,
        1,0,0,0,325,326,5,25,0,0,326,327,5,25,0,0,327,39,1,0,0,0,328,329,
        3,74,37,0,329,330,5,20,0,0,330,331,3,74,37,0,331,41,1,0,0,0,332,
        336,5,31,0,0,333,335,5,58,0,0,334,333,1,0,0,0,335,338,1,0,0,0,336,
        334,1,0,0,0,336,337,1,0,0,0,337,356,1,0,0,0,338,336,1,0,0,0,339,
        350,3,74,37,0,340,344,5,29,0,0,341,343,5,58,0,0,342,341,1,0,0,0,
        343,346,1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,347,1,0,0,0,
        346,344,1,0,0,0,347,349,3,74,37,0,348,340,1,0,0,0,349,352,1,0,0,
        0,350,348,1,0,0,0,350,351,1,0,0,0,351,354,1,0,0,0,352,350,1,0,0,
        0,353,355,5,29,0,0,354,353,1,0,0,0,354,355,1,0,0,0,355,357,1,0,0,
        0,356,339,1,0,0,0,356,357,1,0,0,0,357,361,1,0,0,0,358,360,5,58,0,
        0,359,358,1,0,0,0,360,363,1,0,0,0,361,359,1,0,0,0,361,362,1,0,0,
        0,362,364,1,0,0,0,363,361,1,0,0,0,364,365,5,27,0,0,365,43,1,0,0,
        0,366,370,5,24,0,0,367,369,5,58,0,0,368,367,1,0,0,0,369,372,1,0,
        0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,390,1,0,0,0,372,370,1,0,
        0,0,373,384,3,46,23,0,374,378,5,29,0,0,375,377,5,58,0,0,376,375,
        1,0,0,0,377,380,1,0,0,0,378,376,1,0,0,0,378,379,1,0,0,0,379,381,
        1,0,0,0,380,378,1,0,0,0,381,383,3,46,23,0,382,374,1,0,0,0,383,386,
        1,0,0,0,384,382,1,0,0,0,384,385,1,0,0,0,385,388,1,0,0,0,386,384,
        1,0,0,0,387,389,5,29,0,0,388,387,1,0,0,0,388,389,1,0,0,0,389,391,
        1,0,0,0,390,373,1,0,0,0,390,391,1,0,0,0,391,395,1,0,0,0,392,394,
        5,58,0,0,393,392,1,0,0,0,394,397,1,0,0,0,395,393,1,0,0,0,395,396,
        1,0,0,0,396,398,1,0,0,0,397,395,1,0,0,0,398,399,5,25,0,0,399,45,
        1,0,0,0,400,401,5,19,0,0,401,402,5,20,0,0,402,403,3,74,37,0,403,
        47,1,0,0,0,404,407,5,19,0,0,405,406,5,20,0,0,406,408,3,28,14,0,407,
        405,1,0,0,0,407,408,1,0,0,0,408,409,1,0,0,0,409,410,5,32,0,0,410,
        411,3,74,37,0,411,49,1,0,0,0,412,421,5,19,0,0,413,414,5,26,0,0,414,
        415,3,74,37,0,415,416,5,27,0,0,416,420,1,0,0,0,417,418,5,30,0,0,
        418,420,3,50,25,0,419,413,1,0,0,0,419,417,1,0,0,0,420,423,1,0,0,
        0,421,419,1,0,0,0,421,422,1,0,0,0,422,51,1,0,0,0,423,421,1,0,0,0,
        424,425,5,17,0,0,425,428,5,19,0,0,426,427,5,20,0,0,427,429,3,28,
        14,0,428,426,1,0,0,0,428,429,1,0,0,0,429,430,1,0,0,0,430,431,5,32,
        0,0,431,443,3,74,37,0,432,433,5,17,0,0,433,436,5,19,0,0,434,435,
        5,29,0,0,435,437,5,19,0,0,436,434,1,0,0,0,437,438,1,0,0,0,438,436,
        1,0,0,0,438,439,1,0,0,0,439,440,1,0,0,0,440,441,5,32,0,0,441,443,
        3,76,38,0,442,424,1,0,0,0,442,432,1,0,0,0,443,53,1,0,0,0,444,445,
        3,50,25,0,445,446,7,0,0,0,446,447,3,74,37,0,447,459,1,0,0,0,448,
        451,3,50,25,0,449,450,5,29,0,0,450,452,3,50,25,0,451,449,1,0,0,0,
        452,453,1,0,0,0,453,451,1,0,0,0,453,454,1,0,0,0,454,455,1,0,0,0,
        455,456,5,32,0,0,456,457,3,76,38,0,457,459,1,0,0,0,458,444,1,0,0,
        0,458,448,1,0,0,0,459,55,1,0,0,0,460,461,3,8,4,0,461,57,1,0,0,0,
        462,463,3,8,4,0,463,59,1,0,0,0,464,468,3,66,33,0,465,468,3,62,31,
        0,466,468,3,64,32,0,467,464,1,0,0,0,467,465,1,0,0,0,467,466,1,0,
        0,0,468,61,1,0,0,0,469,470,5,12,0,0,470,471,3,72,36,0,471,472,3,
        58,29,0,472,63,1,0,0,0,473,474,5,13,0,0,474,475,3,58,29,0,475,476,
        5,12,0,0,476,477,5,22,0,0,477,478,3,72,36,0,478,479,5,23,0,0,479,
        65,1,0,0,0,480,482,5,10,0,0,481,483,3,48,24,0,482,481,1,0,0,0,482,
        483,1,0,0,0,483,484,1,0,0,0,484,486,5,21,0,0,485,487,3,72,36,0,486,
        485,1,0,0,0,486,487,1,0,0,0,487,488,1,0,0,0,488,490,5,21,0,0,489,
        491,3,74,37,0,490,489,1,0,0,0,490,491,1,0,0,0,491,494,1,0,0,0,492,
        494,3,68,34,0,493,480,1,0,0,0,493,492,1,0,0,0,494,495,1,0,0,0,495,
        496,3,58,29,0,496,67,1,0,0,0,497,498,5,10,0,0,498,499,5,19,0,0,499,
        502,5,11,0,0,500,503,3,76,38,0,501,503,3,50,25,0,502,500,1,0,0,0,
        502,501,1,0,0,0,503,69,1,0,0,0,504,505,5,7,0,0,505,506,3,72,36,0,
        506,513,3,56,28,0,507,508,5,8,0,0,508,509,3,72,36,0,509,510,3,56,
        28,0,510,512,1,0,0,0,511,507,1,0,0,0,512,515,1,0,0,0,513,511,1,0,
        0,0,513,514,1,0,0,0,514,518,1,0,0,0,515,513,1,0,0,0,516,517,5,9,
        0,0,517,519,3,56,28,0,518,516,1,0,0,0,518,519,1,0,0,0,519,71,1,0,
        0,0,520,521,3,74,37,0,521,73,1,0,0,0,522,523,6,37,-1,0,523,524,5,
        22,0,0,524,525,3,74,37,0,525,526,5,23,0,0,526,536,1,0,0,0,527,536,
        3,34,17,0,528,536,3,76,38,0,529,536,3,50,25,0,530,531,3,50,25,0,
        531,532,7,1,0,0,532,536,1,0,0,0,533,534,5,40,0,0,534,536,3,74,37,
        8,535,522,1,0,0,0,535,527,1,0,0,0,535,528,1,0,0,0,535,529,1,0,0,
        0,535,530,1,0,0,0,535,533,1,0,0,0,536,563,1,0,0,0,537,538,10,7,0,
        0,538,539,5,41,0,0,539,562,3,74,37,7,540,541,10,6,0,0,541,542,7,
        2,0,0,542,562,3,74,37,7,543,544,10,5,0,0,544,545,7,3,0,0,545,562,
        3,74,37,6,546,547,10,4,0,0,547,548,7,4,0,0,548,562,3,74,37,5,549,
        550,10,3,0,0,550,551,5,38,0,0,551,562,3,74,37,4,552,553,10,2,0,0,
        553,554,5,39,0,0,554,562,3,74,37,3,555,556,10,1,0,0,556,557,5,28,
        0,0,557,558,3,74,37,0,558,559,5,20,0,0,559,560,3,74,37,2,560,562,
        1,0,0,0,561,537,1,0,0,0,561,540,1,0,0,0,561,543,1,0,0,0,561,546,
        1,0,0,0,561,549,1,0,0,0,561,552,1,0,0,0,561,555,1,0,0,0,562,565,
        1,0,0,0,563,561,1,0,0,0,563,564,1,0,0,0,564,75,1,0,0,0,565,563,1,
        0,0,0,566,567,5,19,0,0,567,568,5,22,0,0,568,569,3,80,40,0,569,570,
        5,23,0,0,570,77,1,0,0,0,571,572,5,19,0,0,572,573,5,20,0,0,573,574,
        3,28,14,0,574,79,1,0,0,0,575,580,3,74,37,0,576,577,5,29,0,0,577,
        579,3,74,37,0,578,576,1,0,0,0,579,582,1,0,0,0,580,578,1,0,0,0,580,
        581,1,0,0,0,581,584,1,0,0,0,582,580,1,0,0,0,583,585,5,29,0,0,584,
        583,1,0,0,0,584,585,1,0,0,0,585,587,1,0,0,0,586,575,1,0,0,0,586,
        587,1,0,0,0,587,81,1,0,0,0,70,87,89,97,105,111,123,136,139,149,153,
        155,168,172,190,196,207,210,216,223,228,234,237,243,256,262,270,
        276,280,282,287,297,305,311,315,317,322,336,344,350,354,356,361,
        370,378,384,388,390,395,407,419,421,428,438,442,453,458,467,482,
        486,490,493,502,513,518,535,561,563,580,584,586
    ]

class SwagLangParser ( Parser ):

    grammarFileName = "SwagLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'interface'", "'extends'", "'void'", 
                     "'map'", "'set'", "<INVALID>", "'if'", "<INVALID>", 
                     "'else'", "'for'", "'in'", "'while'", "'do'", "'break'", 
                     "'return'", "'defer'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "';'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'?'", "','", "'.'", "'#['", "'='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'&&'", "'||'", "'!'", "'**'", 
                     "'*'", "'/'", "'%'", "'++'", "'--'", "'>'", "'<'", 
                     "'=='", "'!='", "'>='", "'<='", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INTERFACE", "EXTENDS", "VOID", "MAP", 
                      "SET", "TYPE", "IF", "ELSE_IF", "ELSE", "FOR", "IN", 
                      "WHILE", "DO", "BREAK", "RETURN", "DEFER", "ACCESS_MOD", 
                      "BOOL", "IDENT", "COLUMN", "SEMICOL", "L_PAREN", "R_PAREN", 
                      "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "QUESTION", 
                      "COMMA", "DOT", "SET_START", "ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "AND", "OR", "NOT", "EXP", "MUL", "DIV", "MOD", "INC", 
                      "DEC", "GT", "LT", "EQ", "NEQ", "GTE", "LTE", "PLUS", 
                      "MINUS", "STRING", "INT", "FLOAT", "NWLN", "SPACE", 
                      "COMMENT", "INLINE_COMMENT" ]

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
    IDENT=19
    COLUMN=20
    SEMICOL=21
    L_PAREN=22
    R_PAREN=23
    L_CURLY=24
    R_CURLY=25
    L_BRACKET=26
    R_BRACKET=27
    QUESTION=28
    COMMA=29
    DOT=30
    SET_START=31
    ASSIGN=32
    ADD_ASSIGN=33
    SUB_ASSIGN=34
    MUL_ASSIGN=35
    DIV_ASSIGN=36
    MOD_ASSIGN=37
    AND=38
    OR=39
    NOT=40
    EXP=41
    MUL=42
    DIV=43
    MOD=44
    INC=45
    DEC=46
    GT=47
    LT=48
    EQ=49
    NEQ=50
    GTE=51
    LTE=52
    PLUS=53
    MINUS=54
    STRING=55
    INT=56
    FLOAT=57
    NWLN=58
    SPACE=59
    COMMENT=60
    INLINE_COMMENT=61

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 288230376156561530) != 0):
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 4, 5, 6, 17, 19, 22]:
                    self.state = 85
                    self.stmt()
                    pass
                elif token in [58]:
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
            if token in [3, 4, 5, 6, 19, 22]:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 540433057032697080) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 252202680880985336) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 252202680880726016) != 0):
                self.state = 131
                self.expr(0)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==29:
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
            if _la==19:
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
                if _la==29:
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
            if token in [4, 5, 6, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.type_ann()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(SwagLangParser.VOID)
                pass
            elif token in [22]:
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
                    if not (_la==29):
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
            elif token in [19]:
                self.state = 189
                self.match(SwagLangParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
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
                while _la==29:
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
            while _la==58:
                self.state = 213
                self.match(SwagLangParser.NWLN)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
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
                            if not (_la==58):
                                break

                        self.state = 225
                        self.interface_field() 
                    self.state = 230
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==58:
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
            if _la==28:
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
            self.state = 256
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
                self.array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.map_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 254
                self.set_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 255
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
            self.state = 258
            self.match(SwagLangParser.L_BRACKET)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 259
                    self.match(SwagLangParser.NWLN) 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 252202680880726016) != 0):
                self.state = 265
                self.expr(0)
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 266
                        self.match(SwagLangParser.COMMA)
                        self.state = 270
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==58:
                            self.state = 267
                            self.match(SwagLangParser.NWLN)
                            self.state = 272
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 273
                        self.expr(0) 
                    self.state = 278
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 279
                    self.match(SwagLangParser.COMMA)




            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58:
                self.state = 284
                self.match(SwagLangParser.NWLN)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
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
            self.state = 292
            self.match(SwagLangParser.L_CURLY)
            self.state = 293
            self.match(SwagLangParser.L_CURLY)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 294
                    self.match(SwagLangParser.NWLN) 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 252202680880726016) != 0):
                self.state = 300
                self.map_field()
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 301
                        self.match(SwagLangParser.COMMA)
                        self.state = 305
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==58:
                            self.state = 302
                            self.match(SwagLangParser.NWLN)
                            self.state = 307
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 308
                        self.map_field() 
                    self.state = 313
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 314
                    self.match(SwagLangParser.COMMA)




            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58:
                self.state = 319
                self.match(SwagLangParser.NWLN)
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 325
            self.match(SwagLangParser.R_CURLY)
            self.state = 326
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
            self.state = 328
            self.expr(0)
            self.state = 329
            self.match(SwagLangParser.COLUMN)
            self.state = 330
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
            self.state = 332
            self.match(SwagLangParser.SET_START)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 333
                    self.match(SwagLangParser.NWLN) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 252202680880726016) != 0):
                self.state = 339
                self.expr(0)
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 340
                        self.match(SwagLangParser.COMMA)
                        self.state = 344
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==58:
                            self.state = 341
                            self.match(SwagLangParser.NWLN)
                            self.state = 346
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 347
                        self.expr(0) 
                    self.state = 352
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 353
                    self.match(SwagLangParser.COMMA)




            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58:
                self.state = 358
                self.match(SwagLangParser.NWLN)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 364
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
            self.state = 366
            self.match(SwagLangParser.L_CURLY)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 367
                    self.match(SwagLangParser.NWLN) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 373
                self.struct_field()
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 374
                        self.match(SwagLangParser.COMMA)
                        self.state = 378
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==58:
                            self.state = 375
                            self.match(SwagLangParser.NWLN)
                            self.state = 380
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 381
                        self.struct_field() 
                    self.state = 386
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 387
                    self.match(SwagLangParser.COMMA)




            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58:
                self.state = 392
                self.match(SwagLangParser.NWLN)
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 398
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
            self.state = 400
            self.match(SwagLangParser.IDENT)
            self.state = 401
            self.match(SwagLangParser.COLUMN)
            self.state = 402
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
            self.state = 404
            self.match(SwagLangParser.IDENT)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 405
                self.match(SwagLangParser.COLUMN)
                self.state = 406
                self.type_ann()


            self.state = 409
            self.match(SwagLangParser.ASSIGN)
            self.state = 410
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
            self.state = 412
            self.match(SwagLangParser.IDENT)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 419
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [26]:
                        self.state = 413
                        self.match(SwagLangParser.L_BRACKET)
                        self.state = 414
                        self.expr(0)
                        self.state = 415
                        self.match(SwagLangParser.R_BRACKET)
                        pass
                    elif token in [30]:
                        self.state = 417
                        self.match(SwagLangParser.DOT)
                        self.state = 418
                        self.var_ref()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 423
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
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 425
                self.match(SwagLangParser.IDENT)
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 426
                    self.match(SwagLangParser.COLUMN)
                    self.state = 427
                    self.type_ann()


                self.state = 430
                self.match(SwagLangParser.ASSIGN)
                self.state = 431
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(SwagLangParser.ACCESS_MOD)
                self.state = 433
                self.match(SwagLangParser.IDENT)
                self.state = 436 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 434
                    self.match(SwagLangParser.COMMA)
                    self.state = 435
                    self.match(SwagLangParser.IDENT)
                    self.state = 438 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==29):
                        break

                self.state = 440
                self.match(SwagLangParser.ASSIGN)
                self.state = 441
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
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.var_ref()
                self.state = 445
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270582939648) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 446
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.var_ref()
                self.state = 451 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 449
                    self.match(SwagLangParser.COMMA)
                    self.state = 450
                    self.var_ref()
                    self.state = 453 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==29):
                        break

                self.state = 455
                self.match(SwagLangParser.ASSIGN)
                self.state = 456
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
            self.state = 460
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
            self.state = 462
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
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.for_loop()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.while_loop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
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
            self.state = 469
            self.match(SwagLangParser.WHILE)
            self.state = 470
            self.condition()
            self.state = 471
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
            self.state = 473
            self.match(SwagLangParser.DO)
            self.state = 474
            self.loop_body()
            self.state = 475
            self.match(SwagLangParser.WHILE)
            self.state = 476
            self.match(SwagLangParser.L_PAREN)
            self.state = 477
            self.condition()
            self.state = 478
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
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 480
                self.match(SwagLangParser.FOR)

                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 481
                    self.no_acs_mode_var_decl()


                self.state = 484
                self.match(SwagLangParser.SEMICOL)
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 252202680880726016) != 0):
                    self.state = 485
                    self.condition()


                self.state = 488
                self.match(SwagLangParser.SEMICOL)
                self.state = 490
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 489
                    self.expr(0)


                pass

            elif la_ == 2:
                self.state = 492
                self.forin()
                pass


            self.state = 495
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
            self.state = 497
            self.match(SwagLangParser.FOR)
            self.state = 498
            self.match(SwagLangParser.IDENT)
            self.state = 499
            self.match(SwagLangParser.IN)
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 500
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 501
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
            self.state = 504
            self.match(SwagLangParser.IF)
            self.state = 505
            self.condition()
            self.state = 506
            self.conditional_body()
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 507
                self.match(SwagLangParser.ELSE_IF)
                self.state = 508
                self.condition()
                self.state = 509
                self.conditional_body()
                self.state = 515
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 516
                self.match(SwagLangParser.ELSE)
                self.state = 517
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
            self.state = 520
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
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 523
                self.match(SwagLangParser.L_PAREN)
                self.state = 524
                self.expr(0)
                self.state = 525
                self.match(SwagLangParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 527
                self.data()
                pass

            elif la_ == 3:
                self.state = 528
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 529
                self.var_ref()
                pass

            elif la_ == 5:
                self.state = 530
                self.var_ref()
                self.state = 531
                _la = self._input.LA(1)
                if not(_la==45 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.state = 533
                self.match(SwagLangParser.NOT)
                self.state = 534
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 563
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 561
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 537
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 538
                        self.match(SwagLangParser.EXP)
                        self.state = 539
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 540
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 541
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577728) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 542
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 543
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 544
                        _la = self._input.LA(1)
                        if not(_la==53 or _la==54):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 545
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 546
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 547
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8866461766385664) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 548
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 549
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 550
                        self.match(SwagLangParser.AND)
                        self.state = 551
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 552
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 553
                        self.match(SwagLangParser.OR)
                        self.state = 554
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = SwagLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 555
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 556
                        self.match(SwagLangParser.QUESTION)
                        self.state = 557
                        self.expr(0)
                        self.state = 558
                        self.match(SwagLangParser.COLUMN)
                        self.state = 559
                        self.expr(2)
                        pass

             
                self.state = 565
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
            self.state = 566
            self.match(SwagLangParser.IDENT)
            self.state = 567
            self.match(SwagLangParser.L_PAREN)
            self.state = 568
            self.params()
            self.state = 569
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
            self.state = 571
            self.match(SwagLangParser.IDENT)
            self.state = 572
            self.match(SwagLangParser.COLUMN)
            self.state = 573
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
            self.state = 586
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 252202680880726016) != 0):
                self.state = 575
                self.expr(0)
                self.state = 580
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 576
                        self.match(SwagLangParser.COMMA)
                        self.state = 577
                        self.expr(0) 
                    self.state = 582
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 583
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
         




