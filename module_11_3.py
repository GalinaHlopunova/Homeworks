def introspection_info(obj):
    info_dict = {}
    info_dict['type'] = type(obj)
    methods = []
    attributes = dir(obj)
    for attr in dir(obj):
        if callable((getattr(obj, attr))):
            methods.append(attr)
            attributes.remove(attr)
    info_dict['attributes'] = attributes
    info_dict['methods'] = methods
    info_dict['module'] = __name__
    info_dict['callable'] = callable(obj)
    return info_dict


number_info1 = introspection_info(42)
print(number_info1)
number_info1 = introspection_info("Urban")
print(number_info1)
number_info1 = introspection_info([1, 2, 3])
print(number_info1)
