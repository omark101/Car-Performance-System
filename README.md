# Data Collection Phase

## Overview

The data collection phase of this project was a collaborative effort involving multiple team members working diligently to gather, clean, and prepare a comprehensive dataset. This dataset serves as the foundation for our subsequent analyses and models. It's important to note that during this phase, we focused solely on gathering data and did not make any changes to the dataset.

## Table of Contents

- [Overview](#overview)
- [Team Effort and Distribution of Work](#team-effort-and-distribution-of-work)
  - [Data Sources Identification](#data-sources-identification)
  - [Data Scraping and Extraction](#data-scraping-and-extraction)
  - [Data Cleaning and Validation](#data-cleaning-and-validation)
  - [Data Integration](#data-integration)
  - [Documentation and Reporting](#documentation-and-reporting)
- [Challenges and Solutions](#challenges-and-solutions)
- [Conclusion](#conclusion)

## Team Effort and Distribution of Work

### Data Sources Identification

- **Team Members Involved:** [Ahmad Mohsen](https://github.com/Ahmed-Mohsen-2005) , reem , ibrahim , omar , jana 
- **Tasks:** 
  - Identified relevant data sources such as manufacturer websites, trusted information websites , car specification databases, and automotive forums.
  - Assessed the credibility and reliability of each source to ensure high-quality data collection.

### Data Scraping and Extraction

- **Team Members Involved:** Ahmad, Reem, Ibrahim, Omar, Jana
- **Tasks:**
  - Developed and implemented web scraping scripts using `BeautifulSoup` , `requests` and `pandas`.
  - Extracted key specifications and performance metrics for thousands of car models.
  - Extracted additional data to ensure high accuracy in model predictions.
  - Handled dynamic and differently structured content, ensuring consistent data extraction across various websites.
  - Developed and implemented different types of Python scripts to ensure successful data extraction.
  - **Testing and Validation:**
    - Implemented automated tests to verify the accuracy of the data extraction process.
    - Cross-referenced extracted data with trusted sources to ensure reliability.
    - Used data validation techniques to identify and correct inconsistencies or errors in the scraped data.
    - Performed manual checks on a subset of the data to verify the effectiveness of the automated scripts.

### Data Cleaning and Validation

- **Team Members Involved:** Ahmad, Reem, Ibrahim, Omar, Jana
- **Tasks:**
  - As a first step in our dataset, we ensured filling out empty values with `N/A`.
  - Validated data by cross-referencing with multiple sources and rectifying discrepancies.

*Note:* We didn't perform full-scale data cleaning yet; only basic changes were made within the scraping script to handle empty values and similar minor adjustments.


### Data Integration

- **Team Members Involved:** Ahmad , reem , ibrahim , omar , jana 
- **Tasks:**
  - Integrated data from different sources into a centralized datasets.

### Documentation and Reporting

- **Team Members Involved:** Ahmad , reem , ibrahim , omar , jana 
- **Tasks:**
  - Documented the data collection process, including methodologies, challenges, and solutions.
  - Prepared detailed reports and visualizations to summarize the collected data and highlight key insights.

## Challenges and Solutions

- **Challenge:** Handling inconsistent data formats from various sources.
  - **Solution:** Developed robust data parsing scripts and employed regular expressions for pattern matching.
  
- **Challenge:** Ensuring data accuracy and completeness.
  - **Solution:** Conducted thorough validation and cross-referencing with multiple credible sources.

- **Challenge:** Handling different web structures.
  - **Solution:** Developed and implemented dynamic web scraping scripts that adapt to various web structures. Utilized tools such as `BeautifulSoup` to handle both static and dynamic content, ensuring consistent and accurate data extraction across different websites.


## Conclusion

The data collection phase was a critical step in our project, demanding significant effort and collaboration. Each team member played a vital role in ensuring that we gathered an accurate and high-quality dataset that will support our analysis and modeling efforts. The successful completion of this phase lays a strong foundation for the next stages of our project. Importantly, no changes were made to the dataset during this phase, preserving the integrity of the raw data for accurate analysis and ensuring unbiased and reliable results in our subsequent work. This meticulous approach will enable us to draw meaningful insights and develop robust model based on the authentic characteristics of the collected data.

