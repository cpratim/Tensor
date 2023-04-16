# Tensor
##Inspiration
Historically, education has always been a gatekeeper to opportunity. Students are, statistically speaking, more likely to get a job with a proper degree, and the reason for that is simply because of what an education can provide. Yet, even within education, not all experiences are created equal. When teachers do not have sufficient resources to effectively help their students learn, the ability for the students to really grasp key skills or concepts severely declines. As a team, we have all seen this firsthand in some way: whether it be noticing a gap in knowledge and experience in students depending on the schools they came from or volunteering at disadvantaged schools all over the world, there are many improvements to be made in education. For this project, we focus on a specific part: helping disadvantaged teachers teach as best as possible.

##What it does
Our website, Tensor, is a machine learning and computer vision utilizing database that provides the ability to share and access relevant homework, exam, and practice problems that are tailored towards what the teachers need in order to help students learn best. The website takes in questions from contributing teachers and resources like ChatGPT, clusters the data for question attributes, and returns them to querying teachers according to their requests. The app also uses computer vision for uploading files on the contribution page, and has a user login system using Firebase Authentication. With every question that is uploaded, the website generates more questions similar in format to that question based on how popular it is.

##How we built it
We built the website using HTML, CSS, Javascript, Python, Firebase, ChatGPT, OpenCV, and Tesseract. Specifically, we used HTML, CSS, and Javascript for the frontend, ChatGPT for gathering data, OpenCV and Tesseract for recognizing words from files using computer vision, and Python throughout, including for machine learning.

##Challenges we ran into
We ran into many challenges throughout this project, from gathering and parsing data accurately to putting it all together. In particular, we struggled on creating the user authentication, working with Tesseract and OpenCV for computer vision, and designing the frontend of the website.

##Accomplishments that we're proud of
We were proud of our machine learning implementation that is able to intelligently gather its own data and scale at incredible speeds with only a small push to start. Also, the accessibility of this website, along with its many domain names, makes it very user-friendly and impactful. Finally, the computer vision aspect allows more flexibility for generous contributors.

##What we learned
We learned how to use all the libraries that we used, along with designing in figma. We also learned more about machine learning, computer vision, and full stack development.

##What's next for Tensor
Tensor will be expanded to support more images and features, which include functionality with study guides, communication among teachers, and integration of videos. Also, we will be improving our machine learning and computer vision models by expanding data sets, removing biases, and removing outliers. We intend on optimizing our queries and integrating an efficient backend database like convex.
