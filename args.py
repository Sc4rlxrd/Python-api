def msg():
  print('-'*35)
  print('VOLTE SEMPRE CORNO!!!'.center(35))
  print('-'*35)



def the_args2():
  full_name=['Scarlxrd','Dos','Santos','Da','Silva',]
  firstname, lastname, *rest = full_name
  print(firstname, lastname, *rest)
  print(rest)



def the_args(*args):
  first, second, *rest = args
  print(f'Args: {args}')
  print(f'Rest: {rest}')
  print(first,second,rest)

the_args('One','Two','Three','Four','Five','Six')



def dice (*args):
  name, age, *rest = args
  print(f'name: {name}')
  print(f'Age:{age}')
  print(f'Rest: {rest}')
  print(f'Args: {args}')

dice('Scarlxrd',18,'One','Two','Three','Four','Five','Six')


  
def dices(*args):
  first_name, my_age, *rest = args
  print(f'name: {first_name}'.center(10))
  print(f'Age: {my_age}'.center(10))
  print(f'Rest: {rest}'.center(10))
  print(f'Args: {args}'.center(10))
  msg()

dices('Scarlxrd',18,'Eighteen')


def car(*args):
  one_car,two_car,three_car, *rest = args
  print("="*25)
  print(f'first car:{one_car}'.center(10))
  print(f'Two car:{two_car}'.center(10))
  print(f'Three car:{three_car}'.center(10))
  print(f'Rest:{rest}'.center(10))
  print(f"Args:{args}".center(10))
  msg()

car('uno','celta', 'corsa','bmw x3', 'zafira')

