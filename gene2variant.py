#!/usr/bin/env python
import re
import fileinput
import json
import urllib
Lookup = {}
key = raw_input("Please type your gene name, all caps, and press enter: ")
#print var_matches
for line in fileinput.input(['/home/jiawen/data/Homo_sapiens.GRCh37.75.gtf']):
    gene_id_matches = re.findall('gene_id \"(.*?)\";',line)
    gene_name_matches = re.findall('gene_name \"(.*?)\";',line)
    if gene_name_matches:
       if gene_id_matches:
          Lookup[gene_name_matches[0]] = gene_id_matches[0]
         # print "key is " + gene_name_matches[0] + "val is " + gene_id_matches[0]
         #print "gene", key, Lookup[key]
#alternative method but does not work#
#for line in fileinput.input(['/home/jiawen/data/Homo_sapiens.GRCh37.75.gtf']):
#    var_matches = 'gene_id \"(\S*)\"; gene_name \"(.*?)\"\;'
#    gene_id = re.findall(var_matches,line)
#    print gene_id
    #if gene_id == "key":
     
      # print "gene" + str(gene_id)
    #print 'The variants within the gene' + key + '(' + gene_id + ') are:'
   # with urllib.request.urlopen("http://rest.ensembl.org/overlap/id/"gene_id".json?feature=variation")
   # data = json.loads(url.read().decode())
   # for consequence_type in data:
#	print 'Variant {} is a {}.'.format(data['id'], data['consequence_type'])


#PART 2#
url = "http://rest.ensembl.org/overlap/id/" + Lookup[key] + ".json?feature=variation"
response = urllib.urlopen(url)
data = json.loads(response.read())
#make this part a loop#
for i in range (0, len(data)):
    dic = data[i]
    id_names = dic['id']
    consequence_type = dic['consequence_type']
    clinical_result = dic['clinical_significance']
    if clinical_result:
       print "Variant" + id_names + "is a " +  consequence_type.replace("_"," ") + ", and is clinically " + clinical_result[0].upper()
    else: 
       print "Variant" + id_names + "is a " +  consequence_type.replace("_"," ") + ".\n"

