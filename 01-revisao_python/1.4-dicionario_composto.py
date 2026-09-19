#Criando um dicionario composto
funcionarios = {
    101: {
        "nome":"Carlos",
        "Cargo": "Desenvolvedor",
        "habilidades": ["python","C##","Java"] 
    },
    102:{
        "nome":"Mariana",
        "Cargo": "Gerente de projetos",
        "habilidades": ["scrum","gestão"] 
    }
}

print(funcionarios[101]["Cargo"])
print(funcionarios.get(102,{}).get("habilidades"))