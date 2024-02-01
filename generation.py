import openai
import time

openai.api_key = ""

themes = ['']
#texts_amount = int(input("Amount of texts to generate: "))


#while True:
 #   try:
  #      text_size = int(input("Text size in tokens(maximum size is " + str(4070-prompt.count(' ')) + " tokens): "))
   # except ValueError:
   #     print("The value has to be an integer. Try again.")
   # else:
   #     break
for j in themes:
    prompt = f'Write me a text about {j}, at least 2000 words'
    for i in range(3):
        output = openai.completions.create(
            prompt=prompt,
            model="gpt-3.5-turbo-instruct",
            max_tokens=4000
        )
        with open("texts/"+j + "_" + str(i+3)+".txt", "w") as f:
            f.write(output.choices[0].text)
    time.sleep(60)