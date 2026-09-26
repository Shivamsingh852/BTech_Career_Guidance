def get_career_resources(career):
    """
    Module 5: Course & Resource Module
    Returns a dictionary of skills, online courses, and certifications based on the predicted career.
    """
    resources = {
        'Software Engineer': {
            'skills': ['Data Structures & Algorithms', 'System Design', 'Git/GitHub', 'REST APIs'],
            'courses': [
                {'name': 'CS50: Introduction to Computer Science', 'platform': 'edX', 'link': '#'},
                {'name': 'Meta Back-End Developer Professional Certificate', 'platform': 'Coursera', 'link': '#'}
            ],
            'certifications': ['AWS Certified Developer Associate', 'GCP Professional Cloud Developer']
        },
        'Data Scientist': {
            'skills': ['Machine Learning', 'Statistics', 'Python/R', 'SQL', 'Data Visualization'],
            'courses': [
                {'name': 'IBM Data Science Professional Certificate', 'platform': 'Coursera', 'link': '#'},
                {'name': 'Machine Learning Specialization', 'platform': 'Stanford / Coursera', 'link': '#'}
            ],
            'certifications': ['Google Data Analytics Professional Certificate', 'Microsoft Certified: Data Scientist']
        },
        'Business Analyst': {
            'skills': ['Excel', 'SQL', 'Tableau/Power BI', 'Stakeholder Management', 'Agile/Scrum'],
            'courses': [
                {'name': 'Business Analytics Specialization', 'platform': 'Coursera', 'link': '#'},
                {'name': 'SQL for Data Analysis', 'platform': 'Udacity', 'link': '#'}
            ],
            'certifications': ['CBAP (Certified Business Analysis Professional)', 'PMI-PBA']
        },
        'Graphic Designer': {
            'skills': ['Adobe Photoshop', 'Illustrator', 'UI/UX Principles', 'Typography', 'Figma'],
            'courses': [
                {'name': 'Graphic Design Specialization', 'platform': 'CalArts / Coursera', 'link': '#'},
                {'name': 'Google UX Design Professional Certificate', 'platform': 'Coursera', 'link': '#'}
            ],
            'certifications': ['Adobe Certified Professional (Visual Design)']
        },
        'HR Manager': {
            'skills': ['Recruitment', 'Employee Relations', 'Conflict Resolution', 'Labor Law', 'Communication'],
            'courses': [
                {'name': 'HR for People Managers', 'platform': 'Coursera', 'link': '#'},
                {'name': 'People Analytics', 'platform': 'Wharton / Coursera', 'link': '#'}
            ],
            'certifications': ['SHRM-CP', 'PHR (Professional in Human Resources)']
        },
        'Product Manager': {
            'skills': ['Product Strategy', 'User Research', 'Agile Methodologies', 'Wireframing', 'Data Analysis'],
            'courses': [
                {'name': 'Digital Product Management', 'platform': 'UVA / Coursera', 'link': '#'},
                {'name': 'Product Management 101', 'platform': 'Udemy', 'link': '#'}
            ],
            'certifications': ['AIPMM Certified Product Manager', 'CSPO (Certified Scrum Product Owner)']
        }
    }
    
    # Return default generic advice if career string does not match exactly
    return resources.get(career, {
        'skills': ['Continuous Learning', 'Adaptability', 'Problem Solving'],
        'courses': [{'name': 'Search for your career on Coursera or edX', 'platform': 'Various', 'link': '#'}],
        'certifications': ['Check industry-specific certifications']
    })
