def cigar_party(cigar,weekend):
    return not weekend and cigar>=40 and cigar<=60
cigar=int(input())
weekend=input()=="True"
print(cigar_party(cigar,weekend))