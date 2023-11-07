# Installation Guidelines

Follow these steps to install and set up RideShareX on your local machine:

## Prerequisites
- Java Development it (JDK) 8 or higher installed in your system.
- Apache Maven for building the project. You can download it from [Maven Official Website](https://maven.apache.org/download.cgi)

## Clone the Repository
1. Open the terminal window.
2. Clone the RideShareX repository to your local machine:
~~~ bash
git clone https://github.com/kinyarasam/RideShareX.git
~~~

## Build the project.
1. Navigate to the project directory:
~~~ bash
cd RideShareX
~~~
2. Build the project using Maven:
~~~ bash
mvn clean install
~~~

## Configure Database
1. Set up a MySQL or PostgreSQL database.
2. Update the database configuration in `src/main/resources/application.properties` with your database credentials.

## Run the Application
1. After building the project, run the application using Maven:
~~~ bash
mvn spring-boot:run
~~~
2. RideShareX will start, and the application will be accessible at `http://localhost:8080`.

## Access the Application
Open the web browser and navigate to [http://localhost:8080](http://localhost:8080) to access RideShareX.

## Sample User Credentials
- Username: *user@example.com*
- password: *password123*

**Note**: Make sure to change the default credentials and set up appropriate security measures for deployments.

For more detailed information on configuration options and advanced usage, refer to our [full documentation](../README.md).
