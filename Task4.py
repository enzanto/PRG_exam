# The task is uploaded to https://github.com/enzanto/PRG_exam in case indentation or other errors occurs when uploading to Noroff

from stringman import *

newStringObj = sentence("This;is;my;sentence;that;I;want;to;test", ";")

newStringObj.strLength()

strCutted = newStringObj.cutString()

newStringObj.showWordAt(strCutted, 3)
newStringObj.showIndexAt(strCutted, "sentence")
