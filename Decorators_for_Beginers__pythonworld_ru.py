### Create Decorator SELF HANDS ###
def my_shiny_new_decorator(function_to_decorate):
    # WRAPPER FUNCTION
    def the_wrapper_around_the_original_function():
        print("It CODE Working Befor FUNCTION Call")
        function_to_decorate()  # SELF FUNCTION
        print("But It, Handling After CALL FUNCTION")

    return the_wrapper_around_the_original_function


### Function Will Not TOUCH
# def stand_alone_function():
#     print("It SIMPLE ALONE FUNCTION. Will you TOUCH It yet.")


# stand_alone_function()
# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()


### Decorator Function ###
# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("Get Out")


# another_stand_alone_function()


### Some More DECORATOE for ONE FUNCTION ###
# def bread(func):
#     def wrapper():
#         print()
#         func()
#         print("<\________/>")
#         return wrapper
#
#
# def ingredients(func):
#     def wrapper():
#         print("#TOMATO")
#         func()
#         print("~SALAD~")
#
#     return wrapper
#
#
# # def sandwich(food="--BECON--"):
# #     print(food)
#
#
# @bread
# @ingredients
# def sandwich(food="--BECCON--"):
#     print(food)
#
#
# #
#
# # sandwich()
# # sandwich = bread(ingredients(sandwich))
# sandwich()


### ARGUMENTS To Function Transfer By Decorator ###
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print("Look at, what Heppen: ", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#
#     return a_wrapper_accepting_arguments
#
#
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("My name is: ", first_name, last_name)
#
# print_full_name("Vasya", "Pupkin")


### Decorate To Method ###


### Decorator with ARGUMENTS ###
# def decorator_marker():
#     print("It Create DECORATORS! It Will Call one time< Where you Say CREATE DECORATOR.")
#
#     def my_decorator(func):
#         print("It DECORATOR! I Will Cals One Time, at the Moment Decorate FUNCTION.")
#
#         def wrapped():
#             print("It Is WRAPPER Around FUNCTION Where Decorate\n"
#                   "It Will Call Every Time, Where FUNCTION Was Decorate, Was Call"
#                   "I Return Work RESULT fUNCTION WHERE dECORATION")
#             return func()
#
#         print("It Return Wrapper FUNCTION.")
#         return wrapped
#
#     print("It Return DECORATOR.")
#     return my_decorator()
#
#
# # new_decorator = decorator_marker()
# #
# #
# # def decorated_function():
# #     print("It is Function Where Decorate.")
# #
# # decorated_function = new_decorator(decorated_function)
# #
# # decorated_function()
#
# @decorator_marker()
# def decorated_function():
#     print("It FUNCTION Where Will DECORATE.")
#
#
# decorated_function()

#### Any ARGUMENTS TRANSFERS To DECORATOR ###
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("It Create DECORATOR! And Take Following ARGUMENTS: ",
          decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print("It - DECORATOR. And you Could THIS DATA Transfer: ",
              decorator_arg1, decorator_arg2)

        ### Don't Confuse DECORATORS ARGUMENTS and FUNCTIONS ARGUMENTS.
        def wrapped(function_arg1, function_arg2):
            print("It Wrapper around FUNCTION That Needed Decorate.\n"
                  "And It Have Access to ALL ARGUMENTS.\n"
                  "\t- Of DECORATORS: {0}  {1}\n"
                  "\t- and Of FUNCTION: {2}  {3}\n"
                  "It now Required ARGUMENTS Transfer fARTHER\n"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped


@decorator_maker_with_arguments("Leomard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("It FUNCTION Where Required Decorate, and It Know Only SELF ARGUMENTS: {0} {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments("Radzhesh", "Govard")
