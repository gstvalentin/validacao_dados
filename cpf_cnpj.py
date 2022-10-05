from validate_docbr import CPF, CNPJ

class Documento:
    
    @staticmethod
    def cria_documento(documento):
        if CPF().validate(documento):
            return DocCPF(documento)
        elif CNPJ().validate(documento):
            return DocCnpj(documento)
        else:
            raise ValueError('Documento inválido!!!!')


class DocCPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")
    
    def valida(self, documento): #valida cpf
        validador = CPF()
        return validador.validate(documento)

    def __str__(self) -> str: #retorna cpf formatado em str
        return self.formata_cpf()
    
    def formata_cpf(self): #concatena e formata cpf
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj():
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")
        
    def valida(self, documento): #valida cnpj
        validador = CNPJ()
        return validador.validate(documento)
    
    def __str__(self) -> str: #retorna cnpj formatado em str
        return self.formata_cnpj()
    
    def formata_cnpj(self): #concatena e formata cnpj
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
