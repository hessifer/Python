class JavaScriptObject(dict):
    '''JavaScriptObject extends dict'''
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)
            
            
    
if __name__ == '__main__':
    import javascriptobject
    
    jso = javascriptobject.JavaScriptObject({'name': 'Charles'})
    jso.language = 'Python'
    
    print(jso.name)
    print(jso.language)
    print(jso.fake)