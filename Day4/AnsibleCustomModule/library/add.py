#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def add(val1,val2):
    return val1 + val2 

def main():
    module = AnsibleModule( argument_spec=dict( firstValue=dict( type='float' ), secondValue=dict( type='float') ) )

    val1 = module.params['firstValue'] 
    val2 = module.params['secondValue'] 

    response = add( val1, val2 )

    result = dict ( output=response )

    module.exit_json(changed=False, **result )

main()
