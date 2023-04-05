
from datetime import datetime
import random
import time

class BankAcount:
    
    def __init__(self, titular: str = '', open_date = 0, inter_off_date: str = '', acount_numb: int = 0, credit: float = 0,\
                 inter_credit: float = 0, password: str = ''):
        self.__titular = titular
        self.__open_date = open_date
        self.__inter_off_date = inter_off_date
        self.__acount_numb = acount_numb
        self.__credit = credit
        self.__inter_credit = inter_credit
        self.__password = password
        

    @property
    def credit(self):
       return self.__credit
    @credit.setter
    def credit(self, new):
        self.__credit = new

    @property
    def acount_numb(self):
        return self.__acount_numb
    @acount_numb.setter
    def acount_numb(self, new):
        self.__acount_numb = new

    @property
    def open_date(self):
        return self.__open_date
    @open_date.setter
    def open_date(self, new):
        self.__open_date = new

    @property
    def inter_off_date(self):
        return self.__inter_off_date
    @inter_off_date.setter
    def inter_off_date(self, new):
        self.__inter_off_date = new

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, new):
        self.__titular = new

    @property
    def inter_credit(self):
        return self.__inter_credit
    @inter_credit.setter
    def inter_credit(self, new):
        self.__inter_credit = new

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new):
        self.__password = new

    def __str__(self, inst) -> str:
        opendate = str(self.open_date)
        opendate = opendate[:10]
        print(f'\n\n***Bienvenido a BANCO ARENI***\n\nTitular de la cuenta: {self.titular}\nFecha de apertura: {opendate}\n\
Numero de cuenta: {self.acount_numb}\nFondos: {self.credit}\nFondos a plazo fijo: {self.inter_credit}\n')
        return Plazofijo.navigate(inst)
        
        
    def money_out(self, inst):
        credit = inst.credit
        out = 0
        while out < credit:
            print('\n\n *****************Retiro de dinero*****************')
            out = int(input('Ingrese la cantidad que desea retirar: '))
            inst.credit -= out
            options = input('\nGracias por confiar en BANCO ARENI. \n\n Imprimiendo ticket...\n')
            self.navigate(inst)
        else: 
            print(f'\nLo sentimos, no cuenta con fondos suficientes en su cuenta de ahorros. Intente retirar una cantidad menor o igual a {self.credit}.')
            self.navigate(inst)
            

    def money_in(self, inst):
        print('')
        print('*****************Deposito en cuenta de ahorros*****************')
        inn = float(input('Cantidad a ingresar: '))
        if inn <= 20000:
            inst.credit = inst.credit + inn
            options = input('Gracias por confiar en BANCO ARENI. \n\n Imprimiendo ticket...')
            self.navigate(inst)
        else: 
            print('Puede ingresar una cantidad maxima de 20,000 a la vez.')
            self.navigate(inst)



    def transfer(self, inst):
        print('')
        print('Bienvenido@ a BANCO ARENI.\n\n *****************Tranferencias*****************')
        lenght = Plazofijo.acounts_dict
        lenght = len(lenght)
        if lenght < 2:
            print('Lo sentimos, BANCO ARENI necesita al menos dos cuentas para realizar transacciones entre ellas.')
        else:
            out = int(input('Ingrese la cantidad que desea transferir: '))
            name_acount = input('Ingrese el nombre del cuentahabiente: ')
            out_acount = int(input('Ingrese el numero de cuenta destino: '))
        
            if name_acount in Plazofijo.acounts_dict.keys():
                for key, value in Plazofijo.acounts_dict.items():
                    if name_acount == key and Plazofijo.acounts_dict[key].acount_numb == out_acount:
                        if out > inst.credit:
                            print(f'Lo sentimos, no cuenta con fondos suficienes en su cuenta de ahorros. Intente transferir una cantidad menor o igual a\
            {self.credit}.')
                            self.navigate(inst)
                        else:
                            inst.credit = inst.credit - out
                            Plazofijo.acounts_dict[key].credit += out
                            options = input('Gracias por confiar en BANCO ARENI. \n\n Imprimiendo ticket...')
                            self.navigate(inst)
#********************************************************************************************************************************************************************
class Plazofijo(BankAcount):
    cuenta1 = 0
    cuenta2 = 0
    cuenta3 = 0
    acounts_dict = {}
    acounts_dict_sub = {}
    acounts_number = [cuenta1, cuenta2, cuenta3]

    def __init__(self, off_date = 0, open_date = 0, titular: str = '', acount_numb: int = 0, credit: float = 0):
        super().__init__()
        self.__off_date = off_date
        self.__open_date = open_date
        self.__titular = titular
        self.__acount_numb = acount_numb
        self.__credit = credit

    @property
    def off_date(self):
        return self.__off_date
    @off_date.setter
    def off_date(self, new):
        self.__off_date = new

    @property
    def open_date(self):
        return self.__open_date
    @open_date.setter
    def open_date(self, new):
        self.__open_date = new

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, new):
        self.__titular = new

    @property
    def acount_numb(self):
        return self.__acount_numb
    @acount_numb.setter
    def acount_num(self, new):
        self.__acount_numb = new

    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self, new):
        self.__credit = new
    

    def premium_money_in(self, inst):
        print('Bienvenido@ a BANCO ARENI, con nuestras cuentas a plazo fijo usted podra recibir bonificaciones e intereses.\n\n******Ingreso de dinero******')
        take = input('Si ingresa dinero en la cuenta a plazo fijo tendra la posibilidad de recibir una bonificacion del 5 por ciento retirando despues de \
                     la fecha establecida. Fecha...')
        temp = datetime.strptime(take, '%d-%m-%Y').date()
        off_date = datetime.strptime(temp.strftime('%d-%m-%Y'), '%d-%m-%Y')
        inst.inter_off_date = (off_date)
        print(inst.inter_off_date)
        inn = float(input('Cantidad a ingresar: '))
        if inn <= 20000 and inn > 0:
            inst.inter_credit += inn
            self.navigate(inst)
        else: 
            print('Puede ingresar una cantidad maxima de 20,000 a la vez.')
            self.navigate(inst)

    def premium_money_out(self, inst):
        print('Bienvenido@ a BANCO ARENI, con nuestras cuentas a plazo fijo usted podra recibir bonificaciones e intereses.\n\n******Retiro de dinero******')
        print('Si ingresa dinero en la cuenta a plazo fijo tendra la posibilidad de recibir una bonificacion del 5 por ciento retirando despues de \
              la fecha establecida. De lo contrario se le cobrara un interes igual.')
        out = float(input('Cantidad a retirar: '))
        if out < 20000 and out > 0 and out <= inst.inter_credit:
            print(inst.inter_off_date)
            print(inst.open_date)
            if inst.inter_off_date <= inst.open_date:
                inst.inter_credit -= out
                inst.inter_credit += inst.inter_credit * .05
                print('Gracias por confiar en BANCO ARENI.')
                self.navigate(inst)
            else:
                op = input('Si retira fuera de la fecha fijada se cobrara un 5%, de interes, ¿desea continuar?. si/no ')
                if op == 'si':
                    inst.inter_credit -= (inst.inter_credit * .05) + out
                    print('\nGracias por confiar en BANCO ARENI.')
                    self.navigate(inst)
                    
                else:
                    print('\nGracias por confiar en BANCO ARENI.')
                    self.navigate(inst)
        else: 
            print('\nPuede ingresar una cantidad maxima de 20,000 a la vez.')
            self.navigate(inst)


    def create_acount(self):
        titular1 = input('Ingrese su nombre completo: ')
        passw = input('Ingrese una contraseña: ')
        passw1 = input('Ingrese la contraseña de nuevo: ')
        if passw == passw1: 
            temp = datetime.now().date()
            open_date1 = datetime.strptime(temp.strftime('%d-%m-%Y'), '%d-%m-%Y')
            seed = int(time.time())
            random.seed(seed)
            acount_numb1 = int(random.randint(1000000000000, 9999999999999999))
            credit1 = 0
            inter_credit1 = 0
            key = titular1 
            ac = BankAcount(titular = titular1, open_date = open_date1, acount_numb = acount_numb1, credit = credit1, inter_credit = inter_credit1, password = passw)
            Plazofijo.acounts_dict[key] = ac
            #print('')
            print('\n\n¡Felicidades!. Tu cuenta de BANCO ARENI ha sido creada.\n')
            self.navigate(ac)

    

    def join_sesion(self):
        print('************************BANCO ARENI***********************\n\t\t\tIniciar Sesion')
        join = input('Titular de la cuenta: ')
        password1= input('Contraseña: ')
        if join in self.acounts_dict.keys():
            for key, value in self.acounts_dict.items():
                if join == key and value.password == password1:
                    nav = self.acounts_dict[key]
                    self.navigate(nav)

    def show_info(self, inst):
        print(f'\n\n{inst}\n\n')
        return Plazofijo.__str__(inst)
                    
           

    def navigate(self, inst):
        print('')
        option = input('\nBienvenido@ a BANCO ARENI, el banco donde crecen las ideas.\nSeleccione una de las siguientes opciones: \n\n\
1. INGRESAR DINERO. Podras ingresar dinero a tu cuenta.\n\
2. RETIRAR DINERO. Podras retirar dinero de tu cuenta.\n\
3. TRANSFERENCIA. Podras depositar a la cuenta de alguien mas.\n\
4. INGRESO DE DINERO A PLAZO FIJO. Podras ingresar dinero a tu cuenta,\n   y retirarlo en la fecha pactada, de ser asi recibiras \
un beneficio\n   del 5%, de lo contrario deberas abonar el 5% pactado.\n\
5. RETIRO DE DINERO A PLAZO FIJO. Obtendras beneficios si retiras despues de la fecha pactada.\n\
6. CREAR CUENTA VIP. Te permitira disponer de un saldo negativo del 15%, de tu saldo a favor.\n\
7. MOSTRAR INFORMACION DE LA CUENTA.\n\
8. CERRAR SESION.\n\
¿Que deseas hacer? (Elige el numero de la opcion deseada...) ')
    
        if option == '1':
            self.money_in(inst)
        elif option == '2':
            self.money_out(inst)
        elif option == '3':
            self.transfer(inst)
        elif option == '4':
            self.premium_money_in(inst)
        elif option == '5':
            self.premium_money_out(inst)
        elif option == '6':
            None
        elif option == '7':
            self.show_info(inst)
        elif option == '8':
            self.main()

    def main(self):
        option = str(input('\nBIENVENIDO@ A BANCO ARENI, EL BANCO DONDE CRECEN LAS IDEAS.\nEscriba el numero de una de las siguientes opciones: \n\n\
1. CREAR UNA CUENTA. (Al crear una cuenta podra acceder a todos los beneficios que BANCO ARENI ofrece para usted)\n\
2. INICIAR SESION. '))
        obj = Plazofijo()
    
        if option == '1':
            obj.create_acount()
        elif option == '2':
            obj.join_sesion()


                
                   
                   # Se debera modificar el loop de main() para que una vez crada una cuenta y escogida una accion se sigan mostrando las opciones o la opcion de crear otra 
                   # cuenta sin tener que llamar a main() de nuevo.(Esto tomando en cuenta las observaciones de arriba para no dar opcion a crear otra
                   # cuenta hasta no salir de la actual. *****Casi listo, pero no esta implememtado en todos los metodos.

                  