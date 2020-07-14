import functon
sent=str(input("Type a sentence:"))
Data=functon.count_alphabate(sent)
print(Data)
for i in Data:
    print(i,"=",Data[i])