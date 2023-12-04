def slicePromptIfExceedsWarningCtx(symbol,usrselection,doc, promptslice,warningCtx,CTX_MAX):
    if usrselection == "1" or usrselection == '3': #if user selects 1 or 3, it will only return doc before symbol found
        doc = doc.split(symbol)[0]     
    if len(doc) >= CTX_MAX: #if doc length is greater than max context minus warning context
            cut_doc = doc[-promptslice:] #cut the doc from prompt slice to end and return it
            return cut_doc #this will return the cut doc
    return doc
   
