from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        
        if self.cpf_e_valido(documento): #traz erro caso cpf sejá inválido
            self.cpf = documento
        else:
            # print('cpf invalido')
            raise ValueError('CPF é inválido')

    def cpf_e_valido(self, cpf): #valida cpf
        validador = CPF()
        return validador.validate(cpf)
    
    def __str__(self) -> str: #retorna cpf formatado em str
        return self.formata_cpf()
    
    def formata_cpf(self): #concatena e formata cpf
        mascara = CPF()
        return mascara.mask(self.cpf)