import pexpect

username = 'demo'
password = '123'
su="su"
# create a new pexpect spawn object
child = pexpect.spawn(f'{su} {username}')
child.sendline(f'{su} {username}')
# specify the expected password prompt
child.expect('Password:')
child.sendline("123")

# wait for the process to complete
child.expect('$')


child.sendline('whoami')
# print(child.sendline('whoami'))
child.expect('$')
print(child.before)

print(child.after)