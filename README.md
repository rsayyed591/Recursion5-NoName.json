# MedWell

MedWell is a website designed for storing and managing medical reports of patients. It provides a platform where users can securely upload their medical reports and visualize key health indicators through interactive dashboards. This is a Recursion 5.0 hackathon project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Hackathon](#hackathon)

## Installation
To install MedWell, follow these steps:

1. Install Django, PDFPlumber, HTML, CSS, Node.js, SCSS, jQuery, and obtain an API key for OpenAI.
2. Clone the MedWell repository from GitHub.
3. Navigate to the project directory and install dependencies using `pip install -r requirements.txt`.
4. Set up the database and migrate using `python manage.py migrate`.
5. Run the Django server using `python manage.py runserver`.

## Usage

To use MedWell:

1. Access the landing page at [landing_page_url].
2. Register or log in to your account.
3. Navigate to the upload page and upload your medical reports.
4. Once uploaded, the dashboard page will display line graphs showing key health indicators such as homoglobin, RBC count, MCH, etc.
5. The report section highlights any indicators that fall below or above the normal range.

## Contributing

MedWell is an open-source project developed by a group of four individuals during the Recursion 5.0 hackathon. Contributions are welcome!

To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new pull request.

For major changes, please open issue first to discuss the changes you would like to make.

## Hackathon

![Recursion 5.0 Hackathon](hackathon_image_url)

MedWell was developed during the Recursion 5.0 hackathon. Recursion 5.0 is an annual hackathon that brings together developers, designers, and innovators to collaborate and create innovative solutions to real-world problems. Our team of four participated in the hackathon and developed MedWell as an open-source project aiming to improve healthcare management through technology.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
