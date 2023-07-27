class Employee:
    def __init__(self):
        self.authentication = None
        self.role = None

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_authentication(self):
        return self.authentication

    def set_authentication(self, authentication):
        self.authentication = authentication

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma instância de Authentication
    authentication = Authentication("usuario123", "senha456")

    # Criando uma instância de Employee
    employee = Employee()
    employee.set_authentication(authentication)

    # Definindo a função do funcionário
    role = "Gerente"
    employee.set_role(role)

    # Obtendo informações do funcionário
    print("Função do funcionário:", employee.get_role())
    print("Usuário de autenticação:", employee.get_authentication().getUser())
    print("Senha de autenticação:", employee.get_authentication().getPassword())
