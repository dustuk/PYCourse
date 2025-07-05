import csv
import re
import string

def extract_employees_to_csv(job_applications_emails_file):
    """
    Extracts the data of the employees from the given file and adds it to a new csv file.
    
    Parameters:
        job_applications_emails_file: string that contains the name of the file to be read
    """
    def main():
        employees_data = read_employees_data(job_applications_emails_file)
        names, emails, phones, addresses, dobs, experiences = get_employees_data(employees_data)
        add_to_csv(names, emails, phones, addresses, dobs, experiences)
        print("Data has been added to new csv file successfully")

    def read_employees_data(file_name):
        """
        Reads the content of the file with the given name and returns it as a string
        
        Parameters:
            file_name: string that contains the name of the file to be read
        
        Returns:
            string that contains the content of the file
        """
        with open(file_name, encoding="utf-8") as f:
            employees_data = f.read()
        return employees_data

    def get_employees_data(employees_data):
        """
        Gets the data of the employees from the given string and returns the data 
        as six lists of strings: names, emails, phones, addresses, dobs and experiences

        Parameters:
            employees_data: string that contains the data of the employees

        Returns:
            tuple of six lists of strings containing the data of the employees
        """
        names = re.findall(r"Name: (.*?)\n", employees_data)
        emails = re.findall(r"Email: (.*?)\n", employees_data)
        phones = re.findall(r"Phone: (.*?)\n", employees_data)
        addresses = re.findall(r"Address: (.*?)\n", employees_data)
        dobs = re.findall(r"DOB: (.*?)\n", employees_data)
        experiences = re.findall(r"(\d+) year", employees_data)
        return names, emails, phones, addresses, dobs, experiences

    def add_to_csv(names, emails, phones, addresses, dobs, experiences, file_name="employees_data"): 
        """
        Adds the given data to a new csv file with the given file name.

        Parameters:
            names: list of strings that contains the names of the employees
            emails: list of strings that contains the emails of the employees
            phones: list of strings that contains the phones of the employees
            addresses: list of strings that contains the addresses of the employees
            dobs: list of strings that contains the dates of birth of the employees
            experiences: list of strings that contains the experiences of the employees
            file_name: string that contains the name of the file to be written, default is "employees_data"

        Returns:
            None
        """
        with open(f"{file_name}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Email", "Phone", "Address", "DOB", "Experience"])
            for i in range(len(names)):
                writer.writerow([names[i], emails[i], phones[i], addresses[i], dobs[i], experiences[i]])

    main()


def analyze_books_summaries(books_summaries_file):
    """
    Analyzes a text file containing book summaries by performing word frequency analysis
    and extracting unique letters. The analysis includes cleaning the text, counting word
    occurrences, sorting words by frequency, and identifying unique alphabetic characters.
    The results are saved to separate files for words and letters.

    Parameters:
        books_summaries_file: string that contains the file path of the book summaries to be analyzed

    Returns:
        None
    """

    def main():
        """
        Analyzes a text file containing book summaries by performing word frequency analysis
        and extracting unique letters. The analysis includes cleaning the text, counting word
        occurrences, sorting words by frequency, and identifying unique alphabetic characters.
        The results are saved to separate files for words and letters.

        Returns:
            None
        """
        text = read_file(books_summaries_file)
        cleaned_text = clean_text(text)
        word_counts = count_words(cleaned_text)
        sorted_word_counts = sort_words_by_frequency(word_counts)
        unique_letters = extract_unique_letters(cleaned_text)
        save_words_to_file(sorted_word_counts)
        save_letters_to_file(unique_letters)
        print("Analysis completed successfully")


    def read_file(file_name):
        """
        Reads a file and returns its content as a string.

        Parameters:
            file_name: string that contains the file path of the file to be read

        Returns:
            string that contains the content of the file
        """
        with open(file_name, encoding="utf-8") as f:
            text = f.read()
        return text


    
    def clean_text(text):
        """
        Cleans a given text by removing punctuation and converting it to lower case.
        
        Parameters:
            text: string that contains the text to be cleaned
        
        Returns:
            string that contains the cleaned text
        """
        text = text.translate(str.maketrans("", "", string.punctuation))
        text = text.lower()
        return text
    
    def count_words(text):
        """
        Counts the occurrences of each word in the given text.

        Parameters:
            text: string that contains the text to be analyzed

        Returns:
            dictionary with words as keys and their frequency as values
        """
        words = text.split()
        word_counter = {}
        for word in words:
            word_counter[word] = word_counter.get(word, 0) + 1
        return word_counter
    
    def sort_words_by_frequency(word_counter):
        """
        Sorts the given word counter by frequency of the words in descending order.

        Parameters:
            word_counter: dictionary with words as keys and their frequency as values

        Returns:
            list of tuples (word, frequency), sorted by frequency descending
        """
        return sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    
    def extract_unique_letters(text):
        """
        Extracts unique letters from a given text, ignoring non-alphabetic characters.

        Parameters:
            text: string that contains the text to be analyzed

        Returns:
            list of unique alphabetic characters in the given text, sorted in ascending order
        """
        letters = set()
        for letter in text:
            if letter.isalpha():
                letters.add(letter)
        return sorted(letters)

    def save_words_to_file(sorted_word_counts):
        """
        Saves the given word counter to a file named "sorted_words.txt"
        with a header and aligned columns.
        """
        with open("sorted_words.txt", "w", encoding="utf-8") as f:
            f.write(f"{'Word':<20} | {'Frequency'}\n")
            f.write("-" * 35 + "\n")
            for word, freq in sorted_word_counts:
                f.write(f"{word:<20} | {freq}\n")


    def save_letters_to_file(letters):
        """
        Saves the given list of unique letters to a file named "sorted_letters.txt",
        with a header and total count.
        """
        with open("sorted_letters.txt", "w", encoding="utf-8") as f:
            f.write("Unique Letters (Sorted):\n")
            f.write("-" * 25 + "\n")
            for letter in letters:
                f.write(f"{letter}\n")
            f.write("\n")
            f.write(f"Total unique letters: {len(letters)}\n")
        
    main()