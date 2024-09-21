def introspection_info(obj):
    info_dict = {}
    info_dict['type'] = type(obj)
    info_dict['attributes'] = dir(obj)
    info_dict['module'] = __name__
    info_dict['callable'] = callable(obj)
    return info_dict


number_info1 = introspection_info(42)
print(number_info1)
number_info1 = introspection_info("Urban")
print(number_info1)
number_info1 = introspection_info([1, 2, 3])
print(number_info1)
