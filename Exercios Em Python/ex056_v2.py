

        
# class atributos:
#     def __init__(self,nome:str, idade:int, sexo:str): #Definindo a o método inicializador com os atributos da classe
#         self.nome = nome     #Nas linhas onde utilizao self.(atributo) significa que onde eu utilizar esse comando vai ser atribuído ao correspondente.
#         self.idade = idade   #Exemplo: self.idade  -> vai alocar o valor em = idade
#         self.sexo = sexo
               
    
class pessoa():
    def __init__(self,nome:str, idade:int, sexo:str): #Definindo a o método inicializador com os atributos da classe
        self.nome = nome     #Nas linhas onde utilizao self.(atributo) significa que onde eu utilizar esse comando vai ser atribuído ao correspondente.
        self.idade = idade   #Exemplo: self.idade  -> vai alocar o valor em = idade
        self.sexo = sexo

class BancoDados(pessoa):
    def __init__(self, nome, idade, sexo,PosiCastr:int ,ListaPessoas:list):
        super().__init__(nome, idade, sexo)
        self.nome = nome     #Nas linhas onde utilizao self.(atributo) significa que onde eu utilizar esse comando vai ser atribuído ao correspondente.
        self.idade = idade   #Exemplo: self.idade  -> vai alocar o valor em = idade
        self.sexo = sexo
        self.PosiCastr = PosiCastr
        self.ListaPessoas = ListaPessoas
    
    def cadastrar(self):
        novoCadastro = str(input(' Deseja realizar novo cadastro? S/N'))
        if novoCadastro == 'S':
            self.PosiCastr = self.PosiCastr + 1
            self.nome = str(input(' Informe o Nome: '))
            self.idade = int (input('Informe a idade: '))
            self.sexo = str (input('Informe o sexo F/M: '))
            dados = [self.nome, self.idade, self.sexo]
            self.ListaPessoas.append(dados)
def main():
    
    
    RodarSistema = BancoDados("Ermirio", 34, 'M', 12, [lista])
    RodarSistema.cadastrar

if __name__ == "__main__":
    main()           