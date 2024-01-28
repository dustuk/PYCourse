project_num = int(input("Enter a project number: "))


if project_num == 1:
    #Print the following information in the following format.
    countries_and_capitals = [
                            ("Afghanistan", "Kabul"),
                            ("Albania", "Tirana"),
                            ("Algeria", "Algiers"),
                            ("Andorra", "Andorra la Vella"),
                            ("Angola", "Luanda"),
                            ("Antigua and Barbuda", "Saint John's"),
                            ("Argentina", "Buenos Aires"),
                            ("Armenia", "Yerevan"),
                            ("Australia", "Canberra"),
                            ("Austria", "Vienna"),
                            ("Azerbaijan", "Baku"),
                            ("Bahamas", "Nassau"),
                            ("Bahrain", "Manama"),
                            ("Bangladesh", "Dhaka")]
    
    for index, (country, capital) in enumerate(countries_and_capitals, 1):
        print(f"{index}. {country}: {capital}")


if project_num == 2:
    #Using Enumerate make all the sentences in the list upper case and replace spaces with dashes.
    sentences = ['Hello from Codezilla', 'Python Course is awesome', 'I enjoy learning Python with Codezilla']

    for index, sentence in enumerate(sentences):
        print(sentence.upper().replace(' ', '-'))


if project_num == 3:
    #Print the following information in the following format.
    books = [
            ("The 7 Habits of Highly Effective People", "Stephen R. Covey"),
            ("How to Win Friends and Influence People", "Dale Carnegie"),
            ("Atomic Habits", "James Clear"),
            ("The 4-Hour Work Week", "Tim Ferriss"),
            ("Deep Work", "Cal Newport"),
            ("So Good They Can't Ignore You", "Cal Newport"),
            ("Digital Minimalism", "Cal Newport")]
    
    for index, (book, author) in enumerate(books, 1):
        print(f"{index}. Book: {book} - Author: {author}")