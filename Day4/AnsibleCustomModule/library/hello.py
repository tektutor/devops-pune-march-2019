#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return msg

def main():
    module = AnsibleModule( argument_spec=dict( msg=dict( type='str' ) ) )

    val = module.params['msg'] 
    response = sayHello( val )

    result = dict ( output=response )

    module.exit_json(changed=True, **result )

main()
