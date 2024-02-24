<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h3 align="center">VIT Skip Calculator</h3>

  <p align="center">
    Calculates the number of classes you can skip before CAT1, CAT2, and FAT exams without being debarred.
    <br />
    <br />
    <a href="https://github.com/d1by/VIT-Skip-Calculator">View Demo</a>
    ·
    <a href="https://github.com/d1by/VIT-Skip-Calculator/issues">Report Bug</a>
    ·
    <a href="https://github.com/d1by/VIT-Skip-Calculator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
### Built With

* [![Python][Python]][Python-url]
* [![SQLite][SQLite]][SQLite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/d1by/VIT-Skip-Calculator.git
   ```
2. Navigate to the "Time Table" page on VTOP. Copy and paste into ```schedule.txt```
<img src = "https://github.com/d1by/VIT-Skip-Calculator/blob/729998338e1fe9474b0925e3c3ae6ade86807ac8/img/schedule.gif" width=750>

3. Navigate to the "Attendance" page. Copy and paste into ```attendance.txt```
<img src = "https://github.com/d1by/VIT-Skip-Calculator/blob/be869b0198540ebfb5e70b1dd4f725ef32a2a0ce/img/attendance.gif" width=750>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
To run, execute VITSkipCalc.py:

_e.g. from cmd using Python3:_
```py -3 VITSkipCalc.py```

![image](https://github.com/d1by/VIT-Skip-Calculator/assets/108338649/2229563b-9ffb-4367-a039-d1330ba46a81)

For basic modification of database, execute ```createDB.py```

![image](https://github.com/d1by/VIT-Skip-Calculator/assets/108338649/ff70f170-6afb-4793-ab1c-66f54e38b7df)

Semester end date and lab end date are both stored in ```VITSkipCalc.py```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Identify and separate lab classed from theory classes
    - [ ] Currently, the final week of theory-only classes also incorrectly includes lab classes
- [ ] Find better solution for separation of embedded courses _(e.g. BCSE203E, where both theory and lab components share the same source code)_
- [ ] Reduce the number of inputs needed in the database editor for simple tasks _(e.g. updating a day in a database unnecessarily outputs a selection menu after every change)_

#### Additional:
- [ ] Convert into a GO API


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
Dibyanshu Mohapatra - dibym@proton.me

[![Discord](https://img.shields.io/badge/Discord%20Server-%237289DA.svg?logo=discord&logoColor=white)](https://discord.gg/frErDjHStx) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/dibymohapatra)

Project Link: [https://github.com/d1by/VIT-Skip-Calculator](https://github.com/d1by/VIT-Skip-Calculator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [SQLite3 Docs](https://docs.python.org/3/library/sqlite3.html)
* [othneildrew's README Template](https://github.com/othneildrew/Best-README-Template/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/d1by/VIT-Skip-Calculator.svg?style=for-the-badge
[contributors-url]: https://github.com/d1by/VIT-Skip-Calculator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/d1by/VIT-Skip-Calculator.svg?style=for-the-badge
[forks-url]: https://github.com/d1by/VIT-Skip-Calculator/network/members
[stars-shield]: https://img.shields.io/github/stars/d1by/VIT-Skip-Calculator.svg?style=for-the-badge
[stars-url]: https://github.com/d1by/VIT-Skip-Calculator/stargazers
[issues-shield]: https://img.shields.io/github/issues/d1by/VIT-Skip-Calculator.svg?style=for-the-badge
[issues-url]: https://github.com/d1by/VIT-Skip-Calculator/issues
[license-shield]: https://img.shields.io/github/license/d1by/VIT-Skip-Calculator.svg?style=for-the-badge
[license-url]: https://github.com/d1by/VIT-Skip-Calculator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dibymohapatra
[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/Python-limegreen?style=flat-square&logo=Python&logoColor=white
[Python-url]: https://www.python.org/
[SQLite]: https://img.shields.io/badge/SQLite%20-%20darkorange?style=flat-square&logo=SQLite&logoColor=white
[SQLite-url]: https://www.sqlite.org/
