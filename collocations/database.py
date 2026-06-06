"""
Collocation Database
Stores and manages all collocations with variants, examples, and topic information
"""

import json
import os

class CollocationDatabase:
    """Manages collocation data"""
    
    def __init__(self):
        self.collocations = self._load_collocations()
    
    def _load_collocations(self):
        """Load collocations from database"""
        return [
            {
                "id": 1,
                "prompt": "make a",
                "correct_answers": ["decision", "difference", "suggestion", "plan", "contribution"],
                "category": "verbal",
                "difficulty": 1,
                "explanation": "These are the most common words that follow 'make a' in academic writing.",
                "examples": {
                    "Technology": "The development of AI will make a significant difference in how we work.",
                    "Education": "Students must make a decision about their future career paths.",
                    "Environment": "Individual actions can make a contribution to reducing carbon emissions.",
                    "Society": "Good policies make a plan for sustainable development.",
                    "Health": "Regular exercise makes a difference in mental health."
                },
                "variants": ["makes a", "made a", "making a"]
            },
            {
                "id": 2,
                "prompt": "take",
                "correct_answers": ["responsibility", "action", "advantage", "part", "initiative"],
                "category": "verbal",
                "difficulty": 1,
                "explanation": "Common objects for the verb 'take' in academic contexts.",
                "examples": {
                    "Technology": "Companies must take responsibility for data privacy.",
                    "Education": "Teachers take an active role in student development.",
                    "Environment": "Governments should take action on climate change.",
                    "Society": "Citizens can take initiative in community improvement.",
                    "Health": "Patients should take responsibility for their health."
                },
                "variants": ["takes", "took", "taking"]
            },
            {
                "id": 3,
                "prompt": "raise",
                "correct_answers": ["awareness", "questions", "concerns", "standards", "funds"],
                "category": "verbal",
                "difficulty": 1,
                "explanation": "Words that commonly follow 'raise' in essays.",
                "examples": {
                    "Technology": "Social media helps raise awareness about important issues.",
                    "Education": "Teachers raise questions to encourage critical thinking.",
                    "Environment": "NGOs raise concerns about deforestation.",
                    "Society": "Education raises standards in society.",
                    "Health": "Campaigns raise funds for medical research."
                },
                "variants": ["raises", "raised", "raising"]
            },
            {
                "id": 4,
                "prompt": "have an",
                "correct_answers": ["impact", "effect", "influence", "opportunity", "advantage"],
                "category": "verbal",
                "difficulty": 1,
                "explanation": "Common nouns that follow 'have an' in academic writing.",
                "examples": {
                    "Technology": "Technology has an impact on education systems globally.",
                    "Environment": "Pollution has an effect on animal populations.",
                    "Health": "Exercise has an influence on physical well-being.",
                    "Society": "Education has an advantage for personal development.",
                    "Education": "Good mentors have an impact on student success."
                },
                "variants": ["has an", "having an", "had an"]
            },
            {
                "id": 5,
                "prompt": "play a",
                "correct_answers": ["role", "part", "key role", "crucial role", "significant role"],
                "category": "verbal",
                "difficulty": 1,
                "explanation": "Different roles that are commonly discussed in essays.",
                "examples": {
                    "Technology": "Artificial intelligence plays a crucial role in modern industry.",
                    "Education": "Teachers play a key role in student development.",
                    "Environment": "Nature plays a significant role in climate regulation.",
                    "Society": "Family plays a role in character development.",
                    "Health": "Nutrition plays a crucial role in disease prevention."
                },
                "variants": ["plays a", "played a", "playing a"]
            },
            {
                "id": 6,
                "prompt": "lead to",
                "correct_answers": ["increase", "improvement", "decline", "problems", "success"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Consequences that commonly follow 'lead to'.",
                "examples": {
                    "Technology": "Rapid innovation can lead to unforeseen problems.",
                    "Education": "Quality education leads to improvement in society.",
                    "Environment": "Deforestation leads to decline in biodiversity.",
                    "Health": "Exercise leads to improvement in health outcomes.",
                    "Society": "Investment in infrastructure leads to economic growth."
                },
                "variants": ["leads to", "led to", "leading to"]
            },
            {
                "id": 7,
                "prompt": "provide",
                "correct_answers": ["evidence", "support", "information", "opportunities", "services"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Objects commonly provided in academic contexts.",
                "examples": {
                    "Technology": "Research provides evidence of climate change.",
                    "Education": "Schools provide opportunities for skill development.",
                    "Health": "Governments provide healthcare services.",
                    "Society": "Communities provide support for vulnerable groups.",
                    "Environment": "Scientists provide information about ecosystem health."
                },
                "variants": ["provides", "provided", "providing"]
            },
            {
                "id": 8,
                "prompt": "achieve",
                "correct_answers": ["success", "goals", "objectives", "results", "balance"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Common outcomes that can be achieved.",
                "examples": {
                    "Education": "Students achieve success through hard work and dedication.",
                    "Technology": "Companies achieve goals through innovation.",
                    "Society": "Nations achieve objectives through collaboration.",
                    "Health": "People achieve balance through lifestyle management.",
                    "Environment": "Countries achieve sustainability through green policies."
                },
                "variants": ["achieves", "achieved", "achieving"]
            },
            {
                "id": 9,
                "prompt": "contribute to",
                "correct_answers": ["development", "growth", "success", "improvement", "decline"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Outcomes that result from contributions.",
                "examples": {
                    "Technology": "Innovation contributes to economic growth.",
                    "Education": "Quality teaching contributes to student success.",
                    "Environment": "Green energy contributes to environmental improvement.",
                    "Society": "Volunteers contribute to community development.",
                    "Health": "Good diet contributes to health improvement."
                },
                "variants": ["contributes to", "contributed to", "contributing to"]
            },
            {
                "id": 10,
                "prompt": "focus on",
                "correct_answers": ["education", "sustainability", "innovation", "quality", "development"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Common areas of focus in academic discourse.",
                "examples": {
                    "Education": "Schools should focus on developing critical thinking skills.",
                    "Technology": "Tech companies focus on sustainability initiatives.",
                    "Environment": "Conservation efforts focus on biodiversity protection.",
                    "Health": "Healthcare focuses on disease prevention.",
                    "Society": "Development programs focus on poverty reduction."
                },
                "variants": ["focuses on", "focused on", "focusing on"]
            },
            {
                "id": 11,
                "prompt": "address",
                "correct_answers": ["issues", "concerns", "challenges", "problems", "questions"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Common subjects that are addressed in essays.",
                "examples": {
                    "Environment": "The government must address climate change challenges.",
                    "Society": "Policies address social inequality issues.",
                    "Health": "Healthcare systems address public health concerns.",
                    "Education": "Educators address learning challenges.",
                    "Technology": "Regulators address privacy concerns in tech."
                },
                "variants": ["addresses", "addressed", "addressing"]
            },
            {
                "id": 12,
                "prompt": "demonstrate",
                "correct_answers": ["ability", "skills", "knowledge", "competence", "understanding"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Qualities commonly demonstrated in writing.",
                "examples": {
                    "Education": "Students demonstrate competence through examinations.",
                    "Technology": "Engineers demonstrate skills in problem-solving.",
                    "Society": "Leaders demonstrate understanding of social issues.",
                    "Health": "Professionals demonstrate knowledge in their field.",
                    "Environment": "Scientists demonstrate expertise in climate research."
                },
                "variants": ["demonstrates", "demonstrated", "demonstrating"]
            },
            {
                "id": 13,
                "prompt": "significant",
                "correct_answers": ["impact", "influence", "difference", "growth", "change"],
                "category": "adjectival",
                "difficulty": 2,
                "explanation": "Nouns that commonly follow 'significant' in academic writing.",
                "examples": {
                    "Technology": "The internet has had a significant impact on society.",
                    "Education": "Teachers have a significant influence on student development.",
                    "Environment": "Climate change represents a significant challenge.",
                    "Health": "Physical activity shows significant benefits.",
                    "Society": "Education creates significant social change."
                },
                "variants": ["significantly", "significance"]
            },
            {
                "id": 14,
                "prompt": "profound",
                "correct_answers": ["impact", "influence", "effect", "change", "difference"],
                "category": "adjectival",
                "difficulty": 3,
                "explanation": "Strong nouns paired with 'profound' for emphasis.",
                "examples": {
                    "Technology": "AI will have a profound effect on the future of work.",
                    "Society": "Education has a profound influence on individual lives.",
                    "Environment": "Deforestation has profound implications for biodiversity.",
                    "Health": "Mental health has profound effects on overall well-being.",
                    "Education": "Good mentoring creates profound change in students."
                },
                "variants": ["profoundly"]
            },
            {
                "id": 15,
                "prompt": "rapidly",
                "correct_answers": ["growing", "increasing", "developing", "changing", "expanding"],
                "category": "adverbial",
                "difficulty": 2,
                "explanation": "Verbs that often combine with 'rapidly'.",
                "examples": {
                    "Technology": "Technology is rapidly changing society.",
                    "Environment": "Climate change is rapidly accelerating.",
                    "Society": "Urbanization is rapidly increasing globally.",
                    "Health": "Medical breakthroughs are rapidly advancing.",
                    "Education": "Digital learning is rapidly expanding."
                },
                "variants": ["rapid", "rapidity"]
            },
            {
                "id": 16,
                "prompt": "sustainable",
                "correct_answers": ["development", "growth", "practices", "solutions", "future"],
                "category": "adjectival",
                "difficulty": 2,
                "explanation": "Key terms in discussions of sustainability.",
                "examples": {
                    "Environment": "Sustainable development is crucial for the planet.",
                    "Society": "We need sustainable solutions to global problems.",
                    "Technology": "Green technology enables sustainable growth.",
                    "Health": "Sustainable practices improve public health.",
                    "Education": "Schools teach sustainable practices."
                },
                "variants": ["sustainability", "sustainably"]
            },
            {
                "id": 17,
                "prompt": "critical",
                "correct_answers": ["thinking", "skills", "importance", "role", "factor"],
                "category": "adjectival",
                "difficulty": 2,
                "explanation": "Nouns commonly modified by 'critical'.",
                "examples": {
                    "Education": "Critical thinking is essential for academic success.",
                    "Society": "Critical skills are needed in the modern workforce.",
                    "Technology": "Critical analysis of technology is important.",
                    "Health": "Critical care facilities are vital.",
                    "Environment": "Critical environmental issues demand action."
                },
                "variants": ["critically", "criticality"]
            },
            {
                "id": 18,
                "prompt": "fundamental",
                "correct_answers": ["right", "principle", "issue", "problem", "change"],
                "category": "adjectival",
                "difficulty": 3,
                "explanation": "Important concepts described as 'fundamental'.",
                "examples": {
                    "Society": "Education is a fundamental right for all.",
                    "Health": "Health is a fundamental human right.",
                    "Technology": "Data privacy is a fundamental concern.",
                    "Environment": "Climate protection is a fundamental principle.",
                    "Education": "Literacy is fundamental to development."
                },
                "variants": ["fundamentally", "fundamentals"]
            },
            {
                "id": 19,
                "prompt": "remarkable",
                "correct_answers": ["progress", "achievement", "growth", "success", "development"],
                "category": "adjectival",
                "difficulty": 3,
                "explanation": "Positive outcomes described as 'remarkable'.",
                "examples": {
                    "Technology": "Technology has made remarkable progress.",
                    "Education": "Students showed remarkable achievement.",
                    "Health": "Medical science has achieved remarkable breakthroughs.",
                    "Society": "Nations have made remarkable development.",
                    "Environment": "Conservation efforts show remarkable success."
                },
                "variants": ["remarkably"]
            },
            {
                "id": 20,
                "prompt": "widespread",
                "correct_answers": ["adoption", "acceptance", "concern", "problem", "support"],
                "category": "adjectival",
                "difficulty": 2,
                "explanation": "Phenomena that become widespread.",
                "examples": {
                    "Technology": "Widespread adoption of smartphones has transformed society.",
                    "Environment": "Widespread concern about climate change is growing.",
                    "Society": "Widespread support for education reform exists.",
                    "Health": "Widespread awareness of health issues is increasing.",
                    "Education": "Widespread acceptance of online learning."
                },
                "variants": ["widely"]
            },
            {
                "id": 21,
                "prompt": "comprehensive",
                "correct_answers": ["approach", "study", "analysis", "strategy", "framework"],
                "category": "adjectival",
                "difficulty": 3,
                "explanation": "Systemic methods and analyses.",
                "examples": {
                    "Education": "A comprehensive approach to learning is necessary.",
                    "Environment": "Comprehensive environmental protection requires action.",
                    "Society": "Comprehensive policies address social issues.",
                    "Health": "Comprehensive healthcare covers prevention.",
                    "Technology": "Comprehensive analysis of data is essential."
                },
                "variants": ["comprehensively", "comprehensiveness"]
            },
            {
                "id": 22,
                "prompt": "enormous",
                "correct_answers": ["potential", "challenge", "opportunity", "growth", "impact"],
                "category": "adjectival",
                "difficulty": 2,
                "explanation": "Large-scale concepts and challenges.",
                "examples": {
                    "Technology": "AI has enormous potential for innovation.",
                    "Environment": "Climate change poses an enormous challenge.",
                    "Society": "Education offers enormous opportunities.",
                    "Health": "Technology creates enormous health benefits.",
                    "Education": "The internet provides enormous resources."
                },
                "variants": ["enormously"]
            },
            {
                "id": 23,
                "prompt": "overcome",
                "correct_answers": ["challenges", "obstacles", "barriers", "difficulties", "problems"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Difficulties that can be overcome.",
                "examples": {
                    "Society": "Society must overcome social divisions.",
                    "Education": "Students overcome learning challenges through practice.",
                    "Technology": "Innovation helps overcome technical barriers.",
                    "Health": "People overcome health obstacles with support.",
                    "Environment": "Nations overcome environmental challenges through cooperation."
                },
                "variants": ["overcomes", "overcoming", "overcome"]
            },
            {
                "id": 24,
                "prompt": "implement",
                "correct_answers": ["policies", "strategies", "changes", "reforms", "solutions"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Things that are implemented in practice.",
                "examples": {
                    "Society": "Governments implement policies to improve society.",
                    "Education": "Schools implement new teaching strategies.",
                    "Environment": "Countries implement environmental protection measures.",
                    "Technology": "Companies implement cybersecurity solutions.",
                    "Health": "Hospitals implement healthcare reforms."
                },
                "variants": ["implements", "implemented", "implementing"]
            },
            {
                "id": 25,
                "prompt": "evaluate",
                "correct_answers": ["effectiveness", "impact", "performance", "results", "progress"],
                "category": "verbal",
                "difficulty": 3,
                "explanation": "Aspects that are commonly evaluated.",
                "examples": {
                    "Education": "Teachers evaluate student performance regularly.",
                    "Technology": "Companies evaluate the effectiveness of new systems.",
                    "Health": "Researchers evaluate treatment results.",
                    "Society": "Governments evaluate policy impact.",
                    "Environment": "Scientists evaluate conservation progress."
                },
                "variants": ["evaluates", "evaluated", "evaluating"]
            },
            {
                "id": 26,
                "prompt": "enhance",
                "correct_answers": ["quality", "learning", "experience", "performance", "skills"],
                "category": "verbal",
                "difficulty": 2,
                "explanation": "Things that can be enhanced or improved.",
                "examples": {
                    "Education": "Technology enhances the learning experience.",
                    "Health": "Exercise enhances physical well-being.",
                    "Society": "Education enhances quality of life.",
                    "Technology": "New features enhance user experience.",
                    "Environment": "Conservation enhances ecosystem health."
                },
                "variants": ["enhances", "enhanced", "enhancing"]
            },
            {
                "id": 27,
                "prompt": "facilitate",
                "correct_answers": ["communication", "learning", "access", "collaboration", "development"],
                "category": "verbal",
                "difficulty": 3,
                "explanation": "Processes and interactions that are facilitated.",
                "examples": {
                    "Technology": "The internet facilitates global communication.",
                    "Education": "Teachers facilitate student learning and discovery.",
                    "Society": "Infrastructure facilitates economic development.",
                    "Health": "Support groups facilitate healing.",
                    "Environment": "Education facilitates environmental awareness."
                },
                "variants": ["facilitates", "facilitated", "facilitating"]
            },
            {
                "id": 28,
                "prompt": "substantial",
                "correct_answers": ["evidence", "research", "investment", "progress", "increase"],
                "category": "adjectival",
                "difficulty": 3,
                "explanation": "Significant things that are substantial.",
                "examples": {
                    "Technology": "There is substantial evidence of AI's potential.",
                    "Research": "Substantial research supports this conclusion.",
                    "Health": "Substantial investment in healthcare is needed.",
                    "Environment": "Substantial progress has been made.",
                    "Society": "Substantial increases in education funding."
                },
                "variants": ["substantially"]
            },
            {
                "id": 29,
                "prompt": "inevitable",
                "correct_answers": ["change", "consequence", "result", "outcome", "process"],
                "category": "adjectival",
                "difficulty": 3,
                "explanation": "Unavoidable outcomes and processes.",
                "examples": {
                    "Technology": "Technological change is inevitable.",
                    "Society": "Social evolution is an inevitable process.",
                    "Environment": "Climate adaptation is inevitable.",
                    "Health": "Aging is an inevitable biological process.",
                    "Education": "Change in education systems is inevitable."
                },
                "variants": ["inevitably", "inevitability"]
            },
            {
                "id": 30,
                "prompt": "optimize",
                "correct_answers": ["efficiency", "resources", "performance", "process", "outcomes"],
                "category": "verbal",
                "difficulty": 3,
                "explanation": "Systems and processes that are optimized.",
                "examples": {
                    "Technology": "Companies optimize efficiency through automation.",
                    "Education": "Schools optimize learning outcomes.",
                    "Health": "Hospitals optimize patient care processes.",
                    "Environment": "Sustainable practices optimize resource use.",
                    "Society": "Governments optimize public service delivery."
                },
                "variants": ["optimizes", "optimized", "optimizing"]
            }
        ]
    
    def get_collocation(self, collocation_id):
        """Get a specific collocation by ID"""
        for coll in self.collocations:
            if coll["id"] == collocation_id:
                return coll
        return None
    
    def get_all_collocations(self):
        """Get all collocations"""
        return self.collocations
    
    def get_by_difficulty(self, difficulty):
        """Get collocations by difficulty level"""
        return [c for c in self.collocations if c["difficulty"] == difficulty]
    
    def get_by_category(self, category):
        """Get collocations by category"""
        return [c for c in self.collocations if c["category"] == category]