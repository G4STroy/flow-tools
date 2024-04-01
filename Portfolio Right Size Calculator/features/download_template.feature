Feature: Download Excel template
  Scenario: User downloads the Excel template
    Given the application is running
    When the user requests the template download
    Then the Excel template should be downloaded successfully
