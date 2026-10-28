# BlackRoom IA

Versão 1.0.0.

Skill especializada em análise visual de fotografias, selfies e referências UGC, convertendo detalhes de iluminação, cenário, câmera, pose e aparência em prompts JSON estruturados para geração de imagens fotorrealistas.

## Identidade técnica
O material fornecido define a Skill **iPhone Lo-Fi UGC Prompt**, identificador `iphone-lofi-ugc-prompt`. BlackRoom IA é a apresentação deste repositório. O identificador e a especialidade do anexo foram preservados, sem misturar com a Blackroom AI Ultimate de outro projeto.

## Funcionalidades
Análise automática de referência, fidelidade máxima, estética smartphone lo-fi, revisão de prompt e comparação visual. Prioriza composição casual, iluminação cotidiana, aparência natural, roupas, pose, textura e pequenas imperfeições realmente observáveis. Não adiciona grão, distorção ou iluminação cinematográfica como padrão obrigatório.

## Contrato JSON
Um bloco JSON com meta, character_lock, cena, iluminacao, perspectiva_da_camera, assunto e qualidade_da_imagem, preservando os objetos e arrays internos do modelo. A descrição está no [núcleo integral](.agents/skills/iphone-lofi-ugc-prompt/SKILL.md); o [schema](schemas/prompt.schema.json) valida a estrutura. Strings vazias são permitidas para atributos não observáveis.

Valores 9:16, 8k e aparência de câmera frontal no template são exemplos, não fatos de uma referência nem garantia do gerador. A política de fidelidade do núcleo dá precedência à imagem e ao pedido. Não atribuir modelo exato de iPhone, idade exata, identidade ou estado psicológico apenas pela aparência.

## Uso e instalação
Enviar imagem e pedir “Converta esta selfie em JSON mantendo aparência natural”. Para comparação, fornecer referência e resultado acessíveis. Sem imagem, pode criar prompt original a partir de descrição explícita; não alegar análise de foto inexistente.

Ver [instalação](docs/INSTALLATION.md). Copiar `.agents/skills/iphone-lofi-ugc-prompt/` para o local aceito pelo host. Publicação no GitHub não instala automaticamente a Skill no ChatGPT.

## Evidência e limitações
A especificação é documental. Análise visual, preservação facial e comparação de resultados exigem execução real no host. Não há geração automática nem garantia de suporte a campos JSON por fornecedores. O schema organiza instruções, não é payload oficial de API.

O anexo completo está em [fonte](docs/SOURCE_SPECIFICATION.md). O núcleo foi preservado com dois ajustes de formato: remoção de linha inicial vazia e mudança de version para metadata.version. [Auditoria](docs/AUDIT.md).

## Validação e testes
```bash
python -m pip install -r tests/requirements.txt
python tests/validate.py
python tests/test_validator.py
python tests/validate.py --prompt examples/casual-selfie.json
```
Python 3.9+, PyYAML 6.x e jsonschema 4.x. Instalação inicial pode exigir rede; validação local não acessa serviços nem credenciais. Workflow de CI em push e pull request. Verificações estruturais não comprovam qualidade visual ou resultados comportamentais.

## Documentação e manutenção
[Exemplos](examples/README.md), [comparação](docs/COMPARATIVE-TESTS.md), [changelog](CHANGELOG.md) e [contribuições](CONTRIBUTING.md). Oito testes comportamentais fornecidos ainda não executados.

MIT, copyright 2026 mxcapellani. Sem afiliação oficial à Apple ou a fornecedores de geradores de imagem.
