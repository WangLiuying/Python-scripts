library(cidian)
decode_scel(scel = '计算机词汇.scel', output = '计算机词汇.txt', tag = '')
library(stringr)

dicfile = dir('.')
merlist = c()
for(dic in dicfile)
{
  temp = readLines(dic, encoding = 'UTF-8')
  merlist = c(merlist, temp)
  merlist = unique(merlist)
}
merlist = str_replace_all(string = merlist, pattern = '[(),‘’ -?（）:]',replacement = '')
merlist = unique(merlist)

mfile = file('merge_dict.txt',encoding = 'UTF-8')
writeLines(merlist, con = mfile)
close(mfile)
