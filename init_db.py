from database import create_tables

# Função principal que inicializa o banco de dados
def main():
    print("Inicializando o banco de dados...")
    try:
        create_tables()  # Tenta criar as tabelas no banco de dados
        print("Tabelas criadas com sucesso.")  # Informa que as tabelas foram criadas com sucesso
    except Exception as e:
        # Se ocorrer algum erro durante a criação das tabelas, captura a exceção e imprime uma mensagem de erro
        print(f"Erro ao criar as tabelas: {e}")

# Verifica se o script está sendo executado diretamente (não importado como um módulo)
if __name__ == "__main__":
    main()  # Chama a função principal para inicializar o banco de dados