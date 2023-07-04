import time as t

class main():

    while True:

        def main():

            def add():
                
                num1 = float(input("Gib den ersten Summanden ein: \n"))
                num2 = float(input("Gib den zweiten Summanden ein: \n"))

                ans = num1 + num2

                print(ans)



            def sub():

                num1 = float(input("Gib den Subtrahend ein: \n"))
                num2 = float(input("Gib den Minuend ein: \n"))

                ans = num1 - num2

                print(ans)

            def mul():

                num1 = float(input("Gib den ersten Faktor ein: \n"))
                num2 = float(input("Gib den zweiten Faktor ein: \n"))

                ans = num1 * num2

                print(ans)

            def div():

                num1 = float(input("Gib den Dividene ein: \n"))
                num2 = float(input("Gib den Divisor ein: \n"))

                if num2 == 0:
                    print("Teilen durch 0 nicht möglich!")
                    exit()

                ans = num1 / num2

                print(ans)

            inputs = [
                "+",
                "-",
                "*",
                "/"
            ]

            a = "+"
            s = "-"
            m = "*"
            d = "/"
            q = "q"

            x = input(str("Gebe deine Operation ein: \n"))

            if x == a:
                add()
            elif x == s:
                sub()
            elif x == m:
                mul()
            elif x == d:
                div()
            elif x == q:
                exit()
            else:
                print("Keine Gültige Eingabe!\n")
                t.sleep(0.1)
                print("Hier sind alle möglichen Eingaben:\n", inputs)
                main()

        main()
