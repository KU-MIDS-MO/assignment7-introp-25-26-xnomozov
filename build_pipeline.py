def build_pipeline(operation_names):
    """
    operation_names is a list of strings.
    The function must return a new function that applies a sequence 
    of operations to a single input value,in the given order.
    Each string in operation_names represents an operation
    If an unknown operation name is encountered, an error must be raised.
    Calling the returned function should apply all operations sequentially 
    and return the final result.
    
    """
    valid_operations = ['triple','double', 'root', 'square', 'half']
    
    for name in operation_names:
        if name not in valid_operations:
            raise KeyError(f"Unknown operation: {name}")
   
    def pipeline(value):
        result = value  
        
        for name in operation_names:
            try:
                if name == 'triple':
                    result = result * 3
                
                if name == 'double':
                    result = result * 2
                
                elif name == 'root':
                    if result < 0:
                        raise ValueError("Cannot take square root of negative number")
                    result = result ** 0.5
                
                elif name == 'square':
                    result = result * result
                
                elif name == 'half':
                    result = result / 2
                
            except (TypeError, ValueError, ZeroDivisionError) as e:
                raise e 
        
        return result  
    
    return pipeline



my_pipeline = build_pipeline(['root','square', 'double', ])
answer = my_pipeline(33)
print(answer)