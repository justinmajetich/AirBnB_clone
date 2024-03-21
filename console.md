# console commands

## *create*

case 1 : `<command> <Class> <arg 1> ... <arg n> `<br>
case 2 : `<Class> <command> <arg 1> ... <arg n> `<br>
case 3 : `<command> <Class>(<arg 1> ... <arg n>) ` <br>
case 4 : `<Class> <command>(<arg 1> ... <arg n>) ` <br>
case 5 : `<Class>.<command>(<arg 1> ... <arg n>) ` <br>
case 3 : `<command>.<Class>(<arg 1> ... <arg n>) ` <br>

## *examples*
```
create User name="dennis"
User create name="dennis"
create.User name="dennis"
User.create name="dennis"
create User (name="dennis")
User create (name="dennis")
create.User (name="dennis")
User.create (name="dennis")
```
