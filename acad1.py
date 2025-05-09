import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from PIL import Image
import numpy as np
import base64
from io import BytesIO

# Set page configuration
st.set_page_config(
	page_title="Academic Writing for Economics Journals - Dr. Merwan Roudane",
	page_icon="📊",
	layout="wide",
	initial_sidebar_state="expanded"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.4rem;
        font-weight: 600;
        color: #3B82F6;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }
    .highlight {
        background-color: #EFF6FF;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    .caution {
        background-color: #FEF2F2;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #DC2626;
        margin-bottom: 1rem;
    }
    .tip {
        background-color: #ECFDF5;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #10B981;
        margin-bottom: 1rem;
    }
    .example {
        background-color: #F5F3FF;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #8B5CF6;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown("<div class='main-header'>Strategies for Academic Writing in Top Economics Journals</div>",
			unsafe_allow_html=True)
st.markdown("### A Comprehensive Guide by Dr. Merwan Roudane")
st.markdown("---")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = [
	"Introduction",
	"1. Finding Research Ideas",
	"2. Preliminary Research",
	"3. IMRAD Structure",
	"4. Title & Abstract",
	"5. Introduction",
	"6. Literature Review",
	"7. Methodology",
	"8. Results",
	"9. Discussion",
	"10. Conclusion",
	"11. References & Citations",
	"12. Submission Process",
	"13. Responding to Reviewers",
	"14. Resources & Templates"
]
selected_page = st.sidebar.radio("Go to", pages)


# Function to generate a download link for a dataframe
def get_table_download_link(df, filename, text):
	csv = df.to_csv(index=False)
	b64 = base64.b64encode(csv.encode()).decode()
	href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">📥 {text}</a>'
	return href


# Helper function to create two columns with different widths
def create_columns(left_width=2, right_width=1):
	return st.columns([left_width, right_width])


# Helper function to generate a placeholder image
def generate_placeholder_image(width, height, text, bg_color="#f0f0f0", text_color="#333333"):
	img = Image.new('RGB', (width, height), color=bg_color)
	st.image(img, caption=text, use_column_width=True)


# For all pages - top journals info in sidebar
with st.sidebar.expander("Top Economics Journals"):
	top_journals = pd.DataFrame({
		'Journal': [
			'American Economic Review',
			'Quarterly Journal of Economics',
			'Journal of Political Economy',
			'Econometrica',
			'Review of Economic Studies',
			'Journal of Economic Literature',
			'Journal of Finance',
			'Journal of Monetary Economics',
			'Journal of Development Economics',
			'Journal of Economic Perspectives'
		],
		'Impact Factor (2024)': [
			5.24, 8.41, 6.34, 4.87, 5.12,
			7.32, 6.28, 3.89, 3.45, 5.76
		]
	})
	st.dataframe(top_journals, use_container_width=True)
	st.markdown(get_table_download_link(top_journals, "top_economics_journals.csv", "Download Journal List"),
				unsafe_allow_html=True)

# Introduction page
if selected_page == "Introduction":
	st.markdown("<div class='sub-header'>Welcome to the Complete Guide to Academic Writing in Economics</div>",
				unsafe_allow_html=True)

	st.markdown("""
    This comprehensive guide will walk you through the entire process of creating high-quality academic articles 
    for top economics journals, from generating ideas to submitting your polished manuscript.

    Economics is a field where clarity, methodological rigor, and contribution to existing knowledge are paramount. 
    Publishing in top journals requires not only excellent research but also the ability to communicate your findings 
    effectively to both specialized and broader audiences.
    """)

	left_col, right_col = create_columns(2, 1)

	with left_col:
		st.markdown("<div class='section-header'>What This Guide Covers</div>", unsafe_allow_html=True)
		st.markdown("""
        - Identifying promising research questions and gaps in the literature
        - Understanding the IMRAD structure (Introduction, Methods, Results, and Discussion)
        - Crafting compelling titles and abstracts
        - Writing clear and persuasive introductions
        - Conducting and presenting thorough literature reviews
        - Explaining your methodology with appropriate detail
        - Presenting results effectively with tables and figures
        - Discussing implications and limitations of your findings
        - Formatting citations and references according to journal standards
        - Navigating the submission and review process
        """)

	with right_col:
		# Create a dummy figure for publication process
		fig, ax = plt.subplots(figsize=(8, 6))
		stages = ['Idea Generation', 'Research Design', 'Data Collection', 'Analysis', 'Writing', 'Submission',
				  'Revision']
		durations = [2, 3, 4, 5, 6, 1, 3]
		colors = sns.color_palette("Blues", len(stages))

		ax.barh(stages, durations, color=colors)
		ax.set_xlabel('Typical Duration (months)')
		ax.set_title('Economics Publication Process Timeline')
		plt.tight_layout()
		st.pyplot(fig)

	st.markdown("<div class='section-header'>Why Writing Matters in Economics</div>", unsafe_allow_html=True)
	st.markdown("""
    In economics research, your ability to articulate complex ideas clearly is as important as the research itself. 
    The most groundbreaking analysis will have limited impact if readers cannot understand your methods, results, or implications.

    Top economics journals have acceptance rates ranging from 5% to 15%. Standing out requires not only methodological 
    rigor and original contributions but also exceptional presentation of your work.
    """)

	st.markdown(
		"<div class='highlight'>Throughout this guide, I'll share insights from my experience publishing in leading economics journals, with practical advice to help you navigate each stage of the research writing process.</div>",
		unsafe_allow_html=True)

	st.markdown("<div class='section-header'>How to Use This Guide</div>", unsafe_allow_html=True)
	st.markdown("""
    Use the navigation panel on the left to move between sections. While the research and writing process is presented 
    in sequential order, feel free to jump to the specific section that addresses your current needs.

    Each section contains:
    - Key principles and best practices
    - Common pitfalls to avoid
    - Examples from published papers
    - Actionable templates and checklists

    Let's begin the journey of creating impactful economics research papers!
    """)

# Page 1: Finding Research Ideas
elif selected_page == "1. Finding Research Ideas":
	st.markdown("<div class='sub-header'>Finding Promising Research Ideas</div>", unsafe_allow_html=True)

	st.markdown("""
    Developing compelling research ideas is the foundation of successful academic publishing. 
    In economics, the most impactful papers address significant questions with novel approaches or data.
    """)

	# Sources of research ideas
	st.markdown("<div class='section-header'>Sources of Research Ideas</div>", unsafe_allow_html=True)

	idea_sources = {
		"Gap in Literature": "Identify inconsistencies, limitations, or unanswered questions in existing research",
		"Empirical Puzzle": "Observe real-world phenomena that aren't well-explained by current theories",
		"New Data": "Access to novel datasets that allow testing existing theories or exploring new questions",
		"Methodological Innovation": "Apply new econometric or computational methods to existing problems",
		"Policy Relevance": "Address questions with direct implications for economic policy",
		"Interdisciplinary Approach": "Integrate insights from adjacent fields (psychology, sociology, computer science)"
	}

	idea_sources_df = pd.DataFrame({
		'Source': idea_sources.keys(),
		'Description': idea_sources.values()
	})

	st.dataframe(idea_sources_df, use_container_width=True)

	col1, col2 = create_columns()

	with col1:
		st.markdown("<div class='section-header'>Evaluating Potential Research Questions</div>", unsafe_allow_html=True)
		st.markdown("""
        Not all research questions are equally likely to result in high-impact publications. Evaluate your ideas against these criteria:

        1. **Significance**: Does this question address an important economic issue?
        2. **Originality**: Has this specific question been thoroughly addressed before?
        3. **Feasibility**: Do you have access to appropriate data and methods?
        4. **Publication potential**: Would this research interest your target journals?
        5. **Alignment with your expertise**: Can you leverage your existing knowledge?
        """)

		st.markdown(
			"<div class='tip'>💡 **Tip**: Maintain a research journal to regularly record and refine potential research questions. Review emerging literature in your field at least monthly to identify trending topics and gaps.</div>",
			unsafe_allow_html=True)

	with col2:
		# Create visualization for idea evaluation
		labels = ['Significance', 'Originality', 'Feasibility', 'Publication Potential', 'Expertise Alignment']

		# Sample data for two different research ideas
		idea1 = [4, 5, 3, 4, 5]
		idea2 = [5, 3, 4, 5, 2]

		angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
		angles += angles[:1]  # Close the polygon

		idea1 += idea1[:1]
		idea2 += idea2[:1]

		fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
		ax.plot(angles, idea1, 'b-', linewidth=2, label='Idea 1')
		ax.fill(angles, idea1, 'b', alpha=0.1)
		ax.plot(angles, idea2, 'r-', linewidth=2, label='Idea 2')
		ax.fill(angles, idea2, 'r', alpha=0.1)

		ax.set_xticks(angles[:-1])
		ax.set_xticklabels(labels)
		ax.set_yticks([1, 2, 3, 4, 5])
		ax.set_yticklabels(['1', '2', '3', '4', '5'])
		ax.set_ylim(0, 5)

		plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
		plt.title('Research Idea Evaluation')

		st.pyplot(fig)

	st.markdown("<div class='section-header'>Identifying Promising Research Gaps</div>", unsafe_allow_html=True)

	col1, col2 = create_columns()

	with col1:
		st.markdown("""
        To find research gaps in economics, try these systematic approaches:

        1. **Systematic literature review**: Map existing research to identify what's missing
        2. **Follow research agendas**: Look at "future research" sections in influential papers
        3. **Conference attendance**: Note frequently asked questions and unresolved debates
        4. **Journal editor perspectives**: Read editorials about research priorities
        5. **Replicate and extend**: Attempt to replicate key findings and consider extensions
        6. **Cross-field pollination**: Apply methods from other fields to economics questions
        """)

	with col2:
		st.markdown("<div class='example'>**Example: Research Gap Identification**</div>", unsafe_allow_html=True)
		st.markdown("""
        **Original Paper**: "Productivity and Misallocation in General Equilibrium" (Baqaee & Farhi, 2020)

        **Gap Identified**: While existing literature examined misallocation in partial equilibrium, 
        the general equilibrium effects were underexplored.

        **Novel Approach**: Developed a unified framework to analyze how microeconomic shocks and 
        misallocation affect macroeconomic outcomes in general equilibrium.

        **Impact**: Published in The Quarterly Journal of Economics, highly cited for connecting 
        micro-level distortions to macro outcomes.
        """)
	st.markdown(
		"<div class='caution'>⚠️ **Caution**: Avoid salami slicing your research - breaking one substantial idea into multiple smaller publications. Top journals prefer comprehensive treatments of significant questions rather than incremental advances.</div>",
		unsafe_allow_html=True
	)

	st.markdown(
		"<div class='section-header'>Trends in Economics Research (2022-2024)</div>",
		unsafe_allow_html=True
	)

	trends_data = {
		'Research Area': [
			'Machine Learning in Econometrics',
			'Climate Economics',
			'Inequality and Distribution',
			'Digital Economy & Platforms',
			'Behavioral Macroeconomics',
			'Development Microfinance',
			'Health Economics'
		],
		'Publication Trend': [85, 67, 63, 58, 42, 38, 52],
		'Citation Impact': [78, 82, 70, 65, 50, 45, 60]
	}

	trends_df = pd.DataFrame(trends_data)

	fig, ax = plt.subplots(figsize=(10, 6))
	sns.scatterplot(data=trends_df, x='Publication Trend', y='Citation Impact', s=100,
					hue='Research Area', ax=ax)

	ax.set_xlabel('Publication Frequency (Percentile)')
	ax.set_ylabel('Citation Impact (Percentile)')
	ax.set_title('Economics Research Trends (2022-2024)')
	plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

	plt.tight_layout()
	st.pyplot(fig)

	st.markdown("<div class='section-header'>Practical Exercises for Idea Generation</div>", unsafe_allow_html=True)

	st.markdown("""
    1. **Contradiction mapping**: Identify 2-3 papers with contradictory findings on the same topic and brainstorm explanations
    2. **Assumption challenge**: Select an influential paper and list its key assumptions; consider how relaxing each might change results
    3. **Method transfer**: Identify a method from another field and apply it to an economics question
    4. **Extension ideation**: Take a recent paper and list 5 potential extensions or applications
    5. **Real-world anomaly**: Identify economic phenomena that don't align with theoretical predictions
    """)

	st.markdown(
		"<div class='highlight'>Remember: The most successful economics papers combine theoretical insight with empirical rigor and address questions that matter to both academics and policymakers.</div>",
		unsafe_allow_html=True)

# Page 2: Preliminary Research
elif selected_page == "2. Preliminary Research":
	st.markdown("<div class='sub-header'>Preliminary Research & Planning</div>", unsafe_allow_html=True)

	st.markdown("""
    Before diving into full-scale research, thorough preliminary investigation ensures your project 
    is well-defined, feasible, and positioned to make a meaningful contribution.
    """)

	col1, col2 = create_columns(2, 1)

	with col1:
		st.markdown("<div class='section-header'>Scoping Your Research Project</div>", unsafe_allow_html=True)
		st.markdown("""
        Preliminary research involves several key steps:

        1. **Initial literature survey**: Map the intellectual landscape of your topic
        2. **Data availability assessment**: Identify potential data sources and limitations
        3. **Methodological review**: Evaluate analytical approaches used in similar studies
        4. **Resource estimation**: Assess the time, computational resources, and collaborations needed
        5. **Target journal identification**: Select potential journals based on research fit
        """)

		st.markdown(
			"<div class='tip'>💡 **Tip**: Create a one-page research prospectus outlining your research question, potential contribution, data sources, and methodology. Share this with colleagues for early feedback.</div>",
			unsafe_allow_html=True)

	with col2:
		# Create a planning checklist
		planning_checklist = {
			'Task': [
				'Map core literature (25+ papers)',
				'Identify key datasets',
				'Assess methodological approaches',
				'Check target journal requirements',
				'Pilot data collection/analysis',
				'Get feedback on research design',
				'Create project timeline'
			],
			'Importance': [5, 5, 4, 3, 4, 5, 3]
		}

		planning_df = pd.DataFrame(planning_checklist)

		fig, ax = plt.subplots(figsize=(8, 5))
		bars = ax.barh(planning_df['Task'], planning_df['Importance'], color='steelblue')

		ax.set_xlim(0, 5)
		ax.set_xlabel('Priority Level')
		ax.set_title('Preliminary Research Checklist')

		for bar in bars:
			width = bar.get_width()
			ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2, f'{width}/5',
					ha='left', va='center')

		plt.tight_layout()
		st.pyplot(fig)

	st.markdown("<div class='section-header'>Conducting an Effective Literature Review</div>", unsafe_allow_html=True)

	col1, col2 = create_columns()

	with col1:
		st.markdown("""
        A systematic approach to surveying the literature:

        1. **Start with recent review papers** in your area to understand the big picture
        2. **Identify seminal works** that established fundamental concepts and methods
        3. **Map competing explanations or models** for your phenomenon of interest
        4. **Track methodological evolution** in your research area
        5. **Note contradictory findings** that might reveal research opportunities
        6. **Create citation networks** to visualize intellectual lineages and influences
        7. **Investigate recent working papers** for cutting-edge approaches not yet published
        """)

	with col2:
		st.markdown("<div class='section-header'>Literature Organization Tools</div>", unsafe_allow_html=True)

		tools = {
			'Tool': [
				'Zotero',
				'Mendeley',
				'EndNote',
				'Connected Papers',
				'VOSviewer',
				'Obsidian',
				'Research Rabbit'
			],
			'Purpose': [
				'Reference management with PDF organization',
				'Reference and PDF management with social features',
				'Comprehensive reference management',
				'Visual paper relationship mapping',
				'Bibliometric network visualization',
				'Knowledge management with connected notes',
				'AI-powered literature discovery'
			]
		}

		tools_df = pd.DataFrame(tools)
		st.dataframe(tools_df, use_container_width=True)

	st.markdown("<div class='section-header'>Assessing Data Requirements</div>", unsafe_allow_html=True)

	st.markdown("""
    For empirical economics research, data evaluation is critical. Consider:

    - **Data availability**: Is the data publicly available or will you need special access?
    - **Data quality**: Are there known issues with measurement, missing values, or coverage?
    - **Sample size and power**: Is the sample sufficient to detect the effects you're studying?
    - **Time period**: Does the data cover the relevant time period for your research question?
    - **Variables**: Does the dataset include all necessary variables or proxies?
    - **Unit of analysis**: Is the data at the appropriate level (individual, firm, country)?
    - **Data preparation needs**: What cleaning, transformation, or merging will be required?
    """)

	st.markdown(
		"<div class='caution'>⚠️ **Caution**: Data limitations often constrain research design. Be realistic about what conclusions your data will support, and be transparent about limitations in your paper.</div>",
		unsafe_allow_html=True)

	col1, col2 = create_columns()

	with col1:
		st.markdown("<div class='section-header'>Finding Your Contribution</div>", unsafe_allow_html=True)
		st.markdown("""
        In economics, significant contributions typically fall into these categories:

        1. **Theoretical advancement**: Developing new models or extending existing ones
        2. **Empirical novelty**: Testing existing theories with new data or in new contexts
        3. **Methodological innovation**: Introducing new econometric or computational approaches
        4. **Synthesis**: Reconciling conflicting findings or integrating disparate literatures
        5. **Policy relevance**: Providing evidence to inform economic policy decisions

        Clearly articulate your specific contribution early in the planning process. This will 
        guide your research design and help position your paper for publication.
        """)

	with col2:
		st.markdown("<div class='example'>**Example: Contribution Statements**</div>", unsafe_allow_html=True)
		st.markdown("""
        **Weak contribution**: "This paper studies the relationship between inflation and unemployment."

        **Strong contribution**: "This paper extends the Phillips curve model by incorporating expectation 
        heterogeneity across demographic groups. Using novel survey data on inflation expectations 
        spanning 1978-2022, we demonstrate that accounting for this heterogeneity explains 40% of the 
        forecasting errors in standard models during periods of economic transition."

        The strong statement specifies:
        - The theoretical extension (expectation heterogeneity)
        - The data advantage (novel survey data spanning decades)
        - The significance of findings (40% improvement in forecasting)
        - The conditions where the contribution matters most (economic transitions)
        """)

	st.markdown("<div class='section-header'>Timeline Planning for Economics Research</div>", unsafe_allow_html=True)

	# Create timeline for research process
	research_stages = {
		'Stage': [
			'Initial literature review',
			'Research design',
			'Data collection/acquisition',
			'Data cleaning and preparation',
			'Preliminary analysis',
			'Main analysis',
			'Robustness checks',
			'First draft writing',
			'Internal review',
			'Revision',
			'Conference submission',
			'Journal submission'
		],
		'Typical Duration (weeks)': [4, 3, 6, 4, 2, 8, 4, 6, 2, 4, 2, 2],
		'Cumulative Time (weeks)': [4, 7, 13, 17, 19, 27, 31, 37, 39, 43, 45, 47]
	}

	research_df = pd.DataFrame(research_stages)

	fig, ax = plt.subplots(figsize=(10, 8))
	ax.barh(y=research_df['Stage'], width=research_df['Typical Duration (weeks)'],
			left=research_df['Cumulative Time (weeks)'] - research_df['Typical Duration (weeks)'],
			color='skyblue')

	ax.set_xlabel('Weeks')
	ax.set_title('Typical Timeline for Economics Research Project')
	ax.grid(axis='x', linestyle='--', alpha=0.7)

	plt.tight_layout()
	st.pyplot(fig)

	st.markdown(
		"<div class='highlight'>Economics research often takes longer than initially planned. Build in time buffers for unexpected challenges with data access, analysis complexity, or feedback incorporation. Many successful economics papers evolve significantly during the research process.</div>",
		unsafe_allow_html=True)

	st.markdown("<div class='section-header'>Preliminary Research Checklist</div>", unsafe_allow_html=True)

	checklist = """
    <ul>
        <li><input type="checkbox"/> Clearly defined research question with specific scope</li>
        <li><input type="checkbox"/> Comprehensive literature map with identified gaps</li>
        <li><input type="checkbox"/> Assessed data availability and quality</li>
        <li><input type="checkbox"/> Evaluated methodological options and requirements</li>
        <li><input type="checkbox"/> Articulated specific contribution statement</li>
        <li><input type="checkbox"/> Identified target journals and their requirements</li>
        <li><input type="checkbox"/> Created detailed project timeline with milestones</li>
        <li><input type="checkbox"/> Secured necessary resources (data access, software, etc.)</li>
        <li><input type="checkbox"/> Obtained feedback on research design from colleagues</li>
        <li><input type="checkbox"/> Conducted pilot testing of key analytical approaches</li>
    </ul>
    """

	st.markdown(checklist, unsafe_allow_html=True)

# Page 3: IMRAD Structure
elif selected_page == "3. IMRAD Structure":
	st.markdown("<div class='sub-header'>The IMRAD Structure in Economics Papers</div>", unsafe_allow_html=True)

	st.markdown("""
    The IMRAD structure (Introduction, Methods, Results, and Discussion) is the standard organizational 
    framework for empirical research papers in economics. Understanding this structure is essential for 
    crafting papers that meet disciplinary expectations.
    """)

	col1, col2 = create_columns(3, 2)

	with col1:
		st.markdown("<div class='section-header'>IMRAD Overview</div>", unsafe_allow_html=True)
		st.markdown("""
        While economics papers may use different section headings or slightly modified structures, 
        they generally follow the IMRAD logic:

        1. **Introduction**: Research question, motivation, context, and contribution
        2. **Methods**: Theoretical framework, data sources, and empirical strategy
        3. **Results**: Key findings with tables and figures
        4. **And Discussion**: Interpretation, implications, limitations, and conclusion

        Top economics journals expect papers to be comprehensive yet concise, with a clear logical flow 
        between sections. Each section serves a specific purpose in communicating your research.
        """)

	with col2:
		# Create IMRAD structure visualization
		fig, ax = plt.subplots(figsize=(8, 6))

		sections = ['Title & Abstract', 'Introduction', 'Literature Review',
					'Methodology', 'Results', 'Discussion', 'Conclusion', 'References']

		proportions = [5, 15, 10, 20, 25, 15, 5, 5]

		colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(sections)))

		wedges, texts, autotexts = ax.pie(proportions, labels=sections, autopct='%1.0f%%',
										  startangle=90, colors=colors)

		ax.set_title('Typical Section Proportions in Economics Papers')
		plt.setp(autotexts, size=8, weight='bold')
		plt.setp(texts, size=9)

		plt.tight_layout()
		st.pyplot(fig)

	st.markdown("<div class='section-header'>Typical Structure of Economics Papers</div>", unsafe_allow_html=True)

	# Create expandable sections for each IMRAD component
	with st.expander("Title & Abstract (typically 1 page)"):
		st.markdown("""
        - **Title**: Concise, informative description of the paper's focus
        - **Abstract**: Condensed summary of the full paper
            - Research question/objective
            - Methodological approach
            - Key findings
            - Main contribution or implication

        **Length**: 150-250 words (journal-dependent)

        **Example from QJE**: "Monetary Policy and Asset Valuation" (Bianchi, Lettau, and Ludvigson, 2022)

        > We document a form of monetary policy transmission to the stock market operating through variation in risk premiums. We show that risk premium fluctuations are associated with the changing monetary policy stance over time. In contrast to conventional perspectives, however, estimates indicate that risk premiums tend to be high rather than low in periods of monetary accommodation, a pattern we show is consistent with evidence from options prices on monetary policy announcement days. We develop an investment model with monetary policy and ambiguity averse investors to show why accommodative monetary policy can simultaneously stimulate the macroeconomy and generate higher risk premiums.
        """)

	with st.expander("Introduction (typically 3-5 pages)"):
		st.markdown("""
        - Opening hook to engage readers
        - Clear statement of research question
        - Context and motivation for the study
        - Brief overview of relevant literature
        - Explanation of approach and data
        - Preview of key findings
        - Explicit statement of contribution(s)
        - Roadmap of the paper's structure

        **Example Structure**:
        1. Paragraph 1-2: Research question, importance, and key findings
        2. Paragraph 3-4: Background context and motivation
        3. Paragraph 5-6: Brief literature positioning 
        4. Paragraph 7-8: Approach and data overview
        5. Paragraph 9-10: Summary of key results and contributions
        6. Final paragraph: Paper roadmap

        **Distinguishing Features in Economics**:
        - More emphasis on theoretical framework than in some fields
        - Explicit positioning within existing literature
        - Clear articulation of identification strategy for causal claims
        """)

	with st.expander("Literature Review (typically 2-4 pages)"):
		st.markdown("""
        - Comprehensive yet focused review of relevant literature
        - Organization by themes or theoretical perspectives
        - Critical evaluation of existing research
        - Identification of gaps or limitations in prior work
        - Connection to current study's contribution

        **Note**: In some economics papers, especially in top journals, the literature review may be 
        integrated into the introduction rather than appearing as a separate section.

        **Best Practices**:
        - Focus on quality papers in top journals
        - Emphasize recent literature (last 5-10 years)
        - Include seminal papers regardless of age
        - Organize thematically rather than chronologically
        - Critically evaluate rather than merely summarize
        """)

	with st.expander("Methodology (typically 5-8 pages)"):
		st.markdown("""
        - Theoretical framework or model
        - Data sources and sample characteristics
        - Variable construction and measurement
        - Empirical strategy and specification
        - Identification approach for causal inference
        - Estimation procedures

        **Economics-Specific Elements**:
        - Formal mathematical models where relevant
        - Careful discussion of identification strategy
        - Explicit treatment of endogeneity concerns
        - Description of instrumental variables or other approaches
        - Specification tests and robustness checks

        **Example Structure**:
        1. Theoretical model or conceptual framework
        2. Data sources and sample construction
        3. Variable definitions and summary statistics
        4. Econometric specification
        5. Identification strategy
        """)

	with st.expander("Results (typically 6-10 pages)"):
		st.markdown("""
        - Presentation of main findings with tables and figures
        - Interpretation of coefficients and effect sizes
        - Statistical and economic significance
        - Robustness checks and alternative specifications
        - Subgroup analyses or heterogeneity exploration

        **Best Practices**:
        - Present results in logical progression
        - Include well-designed tables and figures
        - Explain key findings in text (don't just refer to tables)
        - Distinguish between statistical and economic significance
        - Address potential concerns proactively
        - Include placebo tests or falsification exercises
        """)

	with st.expander("Discussion (typically 3-5 pages)"):
		st.markdown("""
        - Broader interpretation of findings
        - Connections to theoretical predictions
        - Implications for existing literature
        - Policy relevance or applications
        - Limitations and caveats
        - Directions for future research

        **Key Elements**:
        - Connect empirical findings back to theory
        - Discuss external validity
        - Consider alternative explanations
        - Acknowledge limitations honestly
        - Suggest specific avenues for future work
        """)

	with st.expander("Conclusion (typically 1-2 pages)"):
		st.markdown("""
        - Brief summary of key findings
        - Restatement of main contributions
        - Broader implications or significance
        - Final thought or takeaway message

        **Note**: Avoid introducing new information in the conclusion.

        **Example Conclusion Structure**:
        1. Paragraph 1: Brief restatement of research question and approach
        2. Paragraph 2-3: Summary of key findings
        3. Paragraph 4: Main contributions to literature
        4. Paragraph 5: Broader implications and future directions
        """)

	with st.expander("References & Appendices"):
		st.markdown("""
        - **References**: Complete citations following journal style
        - **Appendices**: Supplementary material
            - Mathematical proofs or detailed derivations
            - Additional robustness checks
            - Data construction details
            - Survey instruments
            - Extended tables or figures

        **Economics Journal Requirements**:
        - Most top economics journals use author-date citation style
        - Appendices may be published online rather than in print
        - Data and code availability statements are increasingly required
        """)

	st.markdown("<div class='section-header'>Adapting IMRAD for Different Types of Economics Papers</div>",
				unsafe_allow_html=True)

	col1, col2 = create_columns()

	with col1:
		st.markdown("<div class='section-header'>Empirical Papers</div>", unsafe_allow_html=True)
		st.markdown("""
        - Standard IMRAD structure
        - Emphasis on:
            - Data sources and collection
            - Econometric methods
            - Identification strategy
            - Robustness checks

        **Example**: "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania" (Card & Krueger)
        """)

		st.markdown("<div class='section-header'>Theory Papers</div>", unsafe_allow_html=True)
		st.markdown("""
        - Modified structure with greater emphasis on model development
        - Typical sections:
            - Introduction
            - Model Setup
            - Equilibrium Analysis
            - Comparative Statics
            - Applications or Extensions
            - Conclusion

        **Example**: "Crime and Punishment: An Economic Approach" (Becker)
        """)

	with col2:
		st.markdown("<div class='section-header'>Methodological Papers</div>", unsafe_allow_html=True)
		st.markdown("""
        - Focus on new econometric or computational approaches
        - Typical sections:
            - Introduction
            - Methodological Framework
            - Monte Carlo Simulations
            - Empirical Application
            - Discussion of Advantages and Limitations

        **Example**: "Regression Discontinuity Designs: A Guide to Practice" (Imbens & Lemieux)
        """)

		st.markdown("<div class='section-header'>Literature Review Papers</div>", unsafe_allow_html=True)
		st.markdown("""
        - Synthesize and evaluate existing literature
        - Typical sections:
            - Introduction
            - Conceptual Framework
            - Thematic Review Sections
            - Research Gaps and Future Directions
            - Conclusion

        **Example**: "What Do We Know About Capital Structure? Some Evidence from International Data" (Rajan & Zingales)
        """)

	st.markdown(
		"<div class='caution'>⚠️ **Caution**: While understanding the typical structure is important, always check the specific requirements of your target journal. Some journals have unique structural preferences or section limitations.</div>",
		unsafe_allow_html=True)

	st.markdown("<div class='section-header'>IMRAD Common Pitfalls in Economics Papers</div>", unsafe_allow_html=True)

	pitfalls = pd.DataFrame({
		'Section': ['Introduction', 'Literature Review', 'Methodology', 'Results', 'Discussion', 'Conclusion'],
		'Common Pitfalls': [
			'Too broad or vague research question; delayed statement of contribution',
			'Unfocused "listing" of papers without synthesis; missing key references',
			'Insufficient detail on identification strategy; inadequate justification of assumptions',
			'Overwhelming tables without clear explanations; focus on statistical but not economic significance',
			'Overinterpreting results beyond what the data support; inadequate treatment of limitations',
			'Merely summarizing previous sections; introducing new material'
		]
	})

	st.dataframe(pitfalls, use_container_width=True)

	st.markdown(
		"<div class='highlight'>The IMRAD structure should serve as a framework, not a constraint. The best economics papers maintain this logical organization while adapting it to effectively communicate their specific contributions.</div>",
		unsafe_allow_html=True)

	st.markdown("<div class='section-header'>IMRAD Structure Template</div>", unsafe_allow_html=True)

	imrad_template = """
    # Title: [Clear, Informative Title That Indicates Key Variables or Relationship]

    ## Abstract
    [Research question/puzzle] [Approach/data] [Key findings] [Main contribution]

    ## 1. Introduction
    - Opening hook and research question
    - Importance and context
    - Brief literature positioning
    - Approach and data overview
    - Preview of findings
    - Specific contributions
    - Paper roadmap

    ## 2. Literature Review (or Theoretical Framework)
    - Relevant theoretical frameworks
    - Empirical evidence on topic
    - Gaps in existing literature
    - Connection to current study

    ## 3. Data and Methodology
    - Theoretical model (if applicable)
    - Data sources and sample construction
    - Variable definitions
    - Summary statistics
    - Econometric specification
    - Identification strategy

    ## 4. Results
    - Main findings
    - Interpretation of coefficients
    - Economic significance
    - Robustness checks
    - Heterogeneity analysis

    ## 5. Discussion
    - Connection to theory
    - Comparison with existing literature
    - Policy implications
    - Limitations and external validity
    - Future research directions

    ## 6. Conclusion
    - Brief summary of question and approach
    - Key findings
    - Main contributions
    - Broader implications

    ## References
    [Formatted according to journal guidelines]

    ## Appendices
    - Mathematical proofs
    - Additional robustness checks
    - Data details
    - Extended tables
    """

	st.code(imrad_template, language='markdown')

# Page 4: Title & Abstract
elif selected_page == "4. Title & Abstract":
	st.markdown("<div class='sub-header'>Crafting Effective Titles and Abstracts</div>", unsafe_allow_html=True)

	st.markdown("""
    Titles and abstracts are the most visible and widely read parts of your paper. They determine whether 
    readers will continue to your full article. In economics, clear, precise titles and informative 
    abstracts are essential for attracting the right audience.
    """)

	st.markdown("<div class='section-header'>Title Strategies for Economics Papers</div>", unsafe_allow_html=True)

	col1, col2 = create_columns(3, 2)

	with col1:
		st.markdown("""
        An effective economics paper title should:

        1. **Clearly indicate the topic and scope**
        2. **Specify key variables or relationships**
        3. **Signal methodology when distinctive**
        4. **Be concise yet informative** (typically 10-15 words)
        5. **Avoid jargon, acronyms, or unnecessary technical terms**
        6. **Be specific rather than general**

        Top economics journals favor straightforward, descriptive titles that clearly communicate 
        the paper's focus. While clever or provocative titles might be memorable, they risk obscuring 
        the paper's content.
        """)

		st.markdown(
			"<div class='tip'>💡 **Tip**: Test your title by asking colleagues if they can accurately describe your paper's focus and contribution based on the title alone.</div>",
			unsafe_allow_html=True)

	with col2:
		st.markdown("<div class='example'>**Examples of Effective Economics Paper Titles**</div>",
					unsafe_allow_html=True)

		title_examples = pd.DataFrame({
			'Title': [
				'The Returns to Education: Evidence from the National Education Longitudinal Study',
				'Monetary Policy and Inequality: A New Channel',
				'Intergenerational Mobility in China: New Evidence from Rural-Urban Migrants',
				'Minimum Wage Effects on Employment, Substitution, and the Teenage Labor Supply',
				'Risk, Uncertainty, and Expected Returns'
			],
			'Why Effective': [
				'Specifies topic (returns to education) and data source',
				'Indicates both variables and novelty ("new channel")',
				'Identifies topic, geographic focus, and sample',
				'Lists specific outcome variables for clarity',
				'Concise but clearly conveys relationships among key concepts'
			]
		})

		st.dataframe(title_examples, use_container_width=True)

	st.markdown("<div class='section-header'>Title Patterns in Top Economics Journals</div>", unsafe_allow_html=True)

	title_patterns = {
		'Pattern': [
			'Question Format',
			'Main Finding',
			'Causal Relationship',
			'Geographic Focus',
			'Methodological Signal',
			'Theoretical Framing',
			'Dual-Part with Colon'
		],
		'Example': [
			'Does Foreign Aid Reduce Poverty?',
			'The Declining Labor Share of Income',
			'How Minimum Wages Affect Employment',
			'Income Inequality in Developing Countries',
			'A Regression Discontinuity Analysis of Educational Returns',
			'Toward a Theory of Optimal Currency Areas',
			'Beyond GDP: Measuring Welfare across Countries'
		],
		'When to Use': [
			'Research directly answers a specific question',
			'Paper presents a robust, novel finding',
			'Study identifies causal mechanisms',
			'Results are specific to certain regions',
			'Novel methodology is a key contribution',
			'Paper develops new theoretical framework',
			'Conceptual framework followed by specific application'
		]
	}

	title_patterns_df = pd.DataFrame(title_patterns)
	st.dataframe(title_patterns_df, use_container_width=True)

	st.markdown(
		"<div class='caution'>⚠️ **Caution**: Avoid overly broad titles like \"An Analysis of Inflation\" or \"Essays on Trade Policy.\" These don't communicate your specific contribution and may signal a lack of focus.</div>",
		unsafe_allow_html=True
	)

	st.markdown(
		"<div class='section-header'>Writing Effective Abstracts</div>",
		unsafe_allow_html=True
	)

	col1, col2 = create_columns()

	with col1:
		st.markdown("""
        A strong economics abstract typically:

        1. **Opens with research question/objective** (1-2 sentences)
        2. **Briefly explains methodology** (1-2 sentences)
        3. **Presents key findings with specific numbers** (2-3 sentences)
        4. **States contribution and implications** (1-2 sentences)

        Within the 150-250 word constraint, every sentence must work efficiently 
        to convey essential information about your paper.

        **Key Elements to Include**:
        - Main research question
        - Key independent and dependent variables
        - Data sources or sample characteristics 
        - Methodological approach
        - Headline results with specific magnitudes
        - Causal identification strategy (if applicable)
        - Primary contribution to literature
        - Policy implications (if applicable)
        """)

	with col2:
		st.markdown("<div class='example'>**Abstract Structure Analysis**</div>", unsafe_allow_html=True)
		st.markdown("""
        From "The Impact of Immigration on the Local Labor Market Outcomes of Blue Collar Workers: Panel Data Evidence" (AEJ: Applied)

        > [QUESTION] Using longitudinal data from the NLSY79, we track the career paths of young low-skilled workers during the 1980s and 1990s, a period of high immigration. [METHODOLOGY] We match each native worker to a local labor market based on their location at age 14 to address selective migration and control for individual fixed effects. [FINDINGS] We find that higher immigration reduces the wages of natives who work in blue collar occupations by 0.6-0.7 percent. [MECHANISM] The negative effect is concentrated among workers with low attachment to their current occupation. [IMPLICATION] Our results suggest that immigration diverts some native workers to different occupations, implying that traditional evaluations of the labor market effects of immigration may be incomplete.

        This abstract:
        - Identifies the research question and time period
        - Explains the data source and methodology
        - Provides specific effect sizes
        - Describes the mechanism
        - Concludes with broader implications
        """)

	st.markdown("<div class='section-header'>Abstract Checklist</div>", unsafe_allow_html=True)

	abstract_checklist = """
    <ul>
        <li><input type="checkbox"/> Clearly states the research question or objective</li>
        <li><input type="checkbox"/> Identifies key variables and relationships studied</li>
        <li><input type="checkbox"/> Mentions data sources and sample characteristics</li>
        <li><input type="checkbox"/> Explains methodology and empirical strategy</li>
        <li><input type="checkbox"/> Reports specific results with magnitudes (not just direction)</li>
        <li><input type="checkbox"/> Indicates statistical and economic significance</li>
        <li><input type="checkbox"/> Articulates main contribution or advance over prior work</li>
        <li><input type="checkbox"/> Notes key implications for theory, policy, or practice</li>
        <li><input type="checkbox"/> Stays within journal's word limit (typically 150-250 words)</li>
        <li><input type="checkbox"/> Contains no citations, tables, or figures</li>
    </ul>
    """

	st.markdown(abstract_checklist, unsafe_allow_html=True)

	st.markdown(
		"<div class='section-header'>Abstract Do's and Don'ts</div>",
		unsafe_allow_html=True
	)

	dos_donts = pd.DataFrame({
		"Do": [
			"State your research question in the first sentence",
			"Include specific effect sizes and magnitudes",
			"Mention your identification strategy",
			"Highlight what's novel about your approach",
			"Use present tense for findings",
			"Be specific about data sources",
			"Mention policy implications if relevant"
		],
		"Don't": [
			"Include literature review or citations",
			"Use jargon or unexplained acronyms",
			"Make broader claims than your results support",
			"Waste words on general background information",
			"Include details of robustness checks",
			"Use vague terms like \"significant effects\"",
			"Introduce concepts not addressed in the paper"
		]
	})

	st.table(dos_donts)

	st.dataframe(dos_donts, use_container_width=True)

	st.markdown("<div class='section-header'>Abstract Templates for Different Types of Economics Papers</div>",
				unsafe_allow_html=True)

	with st.expander("Empirical Paper Abstract Template"):
		st.markdown("""
        ```
        This paper examines [research question] using [data source/sample]. 
        To address [methodological challenge], we employ [identification strategy/econometric approach]. 
        We find that [key independent variable] [increases/decreases] [key dependent variable] by [specific magnitude].
        [Additional finding about heterogeneity, mechanisms, or robustness].
        These results suggest [theoretical or policy implications], contributing to our understanding of [broader economic phenomenon].
        ```

        **Example**:

        > This paper examines how early-life exposure to pollution affects long-term cognitive development using administrative data linking birth records to educational outcomes in North Carolina. To address the endogeneity of pollution exposure, we exploit plant openings and closings as quasi-experimental variation. We find that a one standard deviation increase in early-life exposure to industrial pollution decreases standardized test scores by 0.06 standard deviations and college attendance by 3 percentage points. Effects are larger for disadvantaged populations and persist even after controlling for neighborhood characteristics. These results suggest environmental pollution contributes to inequality through human capital channels, highlighting the importance of considering distributional effects in environmental policy.
        """)

	with st.expander("Theoretical Paper Abstract Template"):
		st.markdown("""
        ```
        This paper develops a [type of model] to analyze [economic phenomenon].
        We show that under [key assumptions], [main theoretical result].
        The model generates several testable predictions: [1-2 key predictions].
        [If applicable] We provide empirical support for these predictions using [data/evidence].
        Our framework helps explain [puzzling economic phenomenon] and offers insights for [policy domain].
        ```

        **Example**:

        > This paper develops a dynamic general equilibrium model to analyze labor market polarization in the presence of skill-biased technological change. We show that under realistic assumptions about task complementarity and substitutability, technological progress leads to non-monotonic effects across the skill distribution. The model generates several testable predictions: employment growth in high and low-skill occupations with declining middle-skill jobs, and corresponding wage patterns reflecting productivity differentials. We provide empirical support for these predictions using occupational data from 18 OECD countries between 1985-2018. Our framework helps explain the simultaneous growth of high and low-skill employment shares and offers insights for education and labor market policies in advanced economies.
        """)

	with st.expander("Methodological Paper Abstract Template"):
		st.markdown("""
        ```
        This paper introduces [new method/approach] for addressing [methodological challenge] in [research area].
        We show that conventional approaches suffer from [limitation] leading to [problem with existing estimates].
        Our method overcomes these limitations by [key methodological innovation].
        Using [simulations/applications], we demonstrate that our approach [specific improvement in performance].
        We apply our method to [empirical application] and find [key results], highlighting [implications of methodological improvement].
        ```

        **Example**:

        > This paper introduces a semiparametric approach for addressing selection bias in panel data economic models with time-varying unobservables. We show that conventional fixed effects estimators suffer from severe bias when selection depends on both permanent and transitory components, leading to incorrect inference in many applications. Our method overcomes these limitations by combining insights from factor structure models with distributional assumptions on the selection process. Using Monte Carlo simulations, we demonstrate that our approach reduces bias by 85% compared to standard methods when selection is endogenous. We apply our method to estimate returns to job training programs and find that conventional approaches underestimate the returns by approximately 40%, highlighting the importance of accounting for time-varying selection.
        """)

	st.markdown(
		"<div class='highlight'>Remember that titles and abstracts are not just summaries—they are marketing tools for your research. In the competitive environment of top economics journals, these elements must quickly convince editors, reviewers, and readers that your paper deserves their attention.</div>",
		unsafe_allow_html=True)

	st.markdown("<div class='section-header'>Title and Abstract Generator Tool</div>", unsafe_allow_html=True)

	col1, col2 = create_columns()

	with col1:
		st.markdown("**Analyze your current title or abstract:**")
	title_input = st.text_input("Enter your current paper title:",
	"The Impact of Monetary Policy on Household Income Inequality")
	abstract_input = st.text_area("Enter your current abstract:",
	"This paper examines the distributional effects of monetary policy.", height = 200)

	with col2:
		st.markdown("**Analysis Results:**")

	# Analyze title
	title_length = len(title_input.split())
	title_feedback = ""

	if title_length < 6:
		title_feedback = "Your title may be too short. Consider adding more specificity about variables or methodology."
	elif title_length > 15:
		title_feedback = "Your title may be too long. Consider making it more concise while retaining key information."
	else:
		title_feedback = "Your title length is within the typical range for economics papers."

	if "effect" in title_input.lower() or "impact" in title_input.lower():
		title_feedback += "\n\nYour title indicates a causal relationship. Ensure your methodology supports causal claims."

	if ":" in title_input:
		title_feedback += "\n\nYou're using a dual-part title structure, which can be effective for combining conceptual framework with specific application."

	# Analyze abstract
	abstract_length = len(abstract_input.split())
	abstract_feedback = ""

	if abstract_length < 50:
		abstract_feedback = "Your abstract is too short. Expand to include methodology, specific findings, and contributions."
	elif abstract_length > 250:
		abstract_feedback = "Your abstract exceeds typical length limits. Consider focusing on the most essential elements."
	else:
		abstract_feedback = f"Your abstract length ({abstract_length} words) is appropriate."

	if "find" in abstract_input.lower() or "result" in abstract_input.lower():
		abstract_feedback += "\n\nYou mention findings, but consider adding specific magnitudes and effect sizes."
	else:
		abstract_feedback += "\n\nConsider adding specific results with numerical values."

	if "contribute" in abstract_input.lower() or "extend" in abstract_input.lower():
		abstract_feedback += "\n\nYou mention contribution, which is essential for positioning your paper."
	else:
		abstract_feedback += "\n\nConsider explicitly stating your contribution to the literature."

	st.markdown(f"**Title Analysis:**\n{title_feedback}")
	st.markdown(f"**Abstract Analysis:**\n{abstract_feedback}")
if selected_page == "1. Title":
    # TODO: fill in your Title‐page code here
    pass

elif selected_page == "2. Abstract":
    # TODO: fill in your Abstract‐page code here
    pass

elif selected_page == "5. Introduction":
    st.markdown(
        "<div class='sub-header'>Crafting Compelling Introductions</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
The introduction is arguably the most critical section of an economics paper. It establishes your research question,
motivates its importance, previews your approach and findings, and articulates your contribution. A well-crafted
introduction significantly increases your chances of publication.
"""
    )


col1, col2 = create_columns(3, 2)

with col1:
		st.markdown("<div class='section-header'>The Structure of Effective Economics Introductions</div>",
					unsafe_allow_html=True)
st.markdown("""
        While there is no single formula, successful economics paper introductions typically include these elements:

        1. **Research question and its importance** (1-2 paragraphs)
           - Clear statement of the specific question
           - Why this question matters (theoretical or practical significance)

        2. **Context and background** (1-2 paragraphs)
           - Relevant economic context
           - Brief overview of the puzzle or debate

        3. **Brief literature positioning** (1-2 paragraphs)
           - Key related literature
           - Identification of the gap or limitation you address

        4. **Your approach** (1-2 paragraphs)
           - Data sources and sample
           - Methodological strategy
           - Identification approach (for causal claims)

        5. **Preview of key findings** (1-3 paragraphs)
           - Major results with specific magnitudes
           - Robustness or sensitivity analyses

        6. **Explicit statement of contributions** (1 paragraph)
           - How your paper advances the literature
           - What's novel about your approach or findings

        7. **Roadmap paragraph** (1 paragraph)
           - Brief outline of subsequent sections
        """)

with col2:
		st.markdown("<div class='example'>**Introduction Length Analysis**</div>", unsafe_allow_html=True)

	# Data for top economics journals
journals = ['American Economic Review', 'Quarterly Journal of Economics',
'Journal of Political Economy', 'Econometrica', 'Review of Economic Studies']
intro_lengths = [5.2, 6.3, 5.8, 4.7, 5.5]  # Average introduction length in pages

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(journals, intro_lengths, color='steelblue')

ax.set_ylabel('Average Introduction Length (pages)')
ax.set_title('Introduction Length in Top Economics Journals')
ax.set_xticklabels(journals, rotation=45, ha='right')

for bar in bars:
	height = bar.get_height()
ax.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
f'{height}', ha = 'center', va = 'bottom')

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
        **Key Takeaway**: Introductions in top economics journals typically range from 4-7 pages (double-spaced), 
        constituting about 15-20% of the paper's total length. The introduction should be comprehensive yet focused.
        """)

st.markdown("<div class='section-header'>Opening Paragraph Strategies</div>", unsafe_allow_html=True)

st.markdown("""
    The opening paragraph is crucial—it's your chance to hook readers and establish the importance of your research. 
    Effective opening strategies in economics include:
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("<div class='section-header'>Effective Opening Approaches</div>", unsafe_allow_html=True)
st.markdown("""
        1. **Puzzling empirical phenomenon**
           - Begin with an intriguing pattern or fact that your paper explains

        2. **Clear research question**
           - Directly state the question your paper addresses

        3. **Policy relevance**
           - Connect your research to significant policy debates

        4. **Theoretical controversy**
           - Highlight competing theories your paper helps adjudicate

        5. **Economic importance**
           - Emphasize the magnitude or prevalence of the issue
        """)

with col2:
	st.markdown("<div class='example'>**Examples of Strong Opening Paragraphs**</div>", unsafe_allow_html=True)
st.markdown("""
        **Puzzling phenomenon approach**:
        > Despite substantial public investment in college financial aid, large gaps in college attendance by family income persist. In 2015, 78 percent of students from high-income families enrolled in college immediately after high school graduation, compared to just 46 percent of students from low-income families (NCES 2017). This paper investigates whether information constraints contribute to this socioeconomic gap.

        **Policy relevance approach**:
        > Central banks around the world have increasingly adopted inflation targeting as their monetary policy framework, with over 40 countries now implementing some form of this approach. Yet its effects on macroeconomic performance remain contested. This paper provides new evidence on whether inflation targeting improves economic outcomes in developing economies.
        """)

st.markdown(
    """<div class='caution'>⚠️ **Caution**: Avoid opening with broad generalizations ("Since the beginning of time..."), dictionary definitions, or lengthy literature reviews. These approaches fail to immediately communicate your specific contribution and may signal a lack of focus.</div>""",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='section-header'>Articulating Your Contribution</div>",
    unsafe_allow_html=True
)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Clearly stating your contribution is essential in economics papers. This typically appears 
        toward the end of the introduction after you've presented your approach and key findings.

        Your contribution statement should:

        1. **Be explicit** - Use clear language like "We contribute to the literature by..."
        2. **Be specific** - Identify exactly what's new (data, method, findings)
        3. **Connect to literature** - Show how you extend or challenge existing research
        4. **Distinguish components** - If multiple contributions, list them separately
        5. **Avoid overstatement** - Make claims proportional to your evidence

        In top economics journals, authors typically articulate 2-4 specific contributions.
        """)

with col2:
	st.markdown("<div class='example'>**Example Contribution Statements**</div>", unsafe_allow_html=True)
st.markdown("""
        From "The Impact of Minimum Wages on Job Creation and Employment" (hypothetical):

        > This paper makes three contributions to the literature on minimum wage effects. First, we introduce a new identification strategy that exploits policy discontinuities at state borders, addressing the endogeneity concerns in previous studies. Second, we provide the first estimates of minimum wage impacts on both job creation and job destruction margins using matched employer-employee data. Third, we develop a theoretical framework that explains the heterogeneous effects we observe across firm sizes and industries. Together, these contributions help reconcile conflicting findings in the existing minimum wage literature.

        **Why Effective**:
        - Clearly numbers distinct contributions
        - Specifies what's novel about each (method, data, theory)
        - Connects to existing literature
        - Explains significance (reconciling conflicting findings)
        """)

st.markdown("<div class='section-header'>Literature Positioning</div>", unsafe_allow_html=True)

st.markdown("""
    In economics introductions, you must position your work within the relevant literature. This typically 
    comes early in the introduction, though sometimes after presenting your research question.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Effective literature positioning:

        1. **Groups literature thematically** rather than chronologically
        2. **Focuses on the most relevant papers** rather than being exhaustive
        3. **Identifies specific limitations** or gaps you address
        4. **Distinguishes your approach** from previous work
        5. **Cites appropriate works** based on journal and topic

        For most empirical papers, 1-2 paragraphs in the introduction should suffice for literature positioning, 
        with more detailed discussion reserved for a separate literature section if needed.
        """)

with col2:
	st.markdown("<div class='example'>**Example Literature Positioning**</div>", unsafe_allow_html=True)
st.markdown("""
        > Our paper relates to three strands of literature. First, we build on studies examining the relationship between financial development and economic growth (King and Levine 1993; Rajan and Zingales 1998; Levine 2005). While this literature establishes a positive correlation between financial development and growth, identification challenges have made causal interpretations difficult. Second, we contribute to research on banking deregulation (Jayaratne and Strahan 1996; Beck et al. 2010), which has focused primarily on firm-level outcomes rather than distributional effects. Finally, our paper connects to the growing literature on income inequality (Piketty and Saez 2003; Autor et al. 2008) by examining how financial sector policies affect the income distribution. Our contribution is to combine these literatures using a novel identification strategy that allows us to estimate the causal impact of financial development on both growth and inequality.
        """)

st.markdown("<div class='section-header'>Previewing Key Findings</div>", unsafe_allow_html=True)

st.markdown("""
    After introducing your research question and approach, you should preview your main findings. 
    This typically appears in the middle or latter part of the introduction.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Effective presentation of findings in the introduction:

        1. **Provides specific magnitudes** and effect sizes, not just directions
        2. **Highlights the most important results** (not every finding)
        3. **Connects results to the research question**
        4. **Mentions key robustness checks** or sensitivity analyses
        5. **Acknowledges limitations** where appropriate

        Be clear about what you find, but avoid excessive technical detail in the introduction. 
        The goal is to communicate the key takeaways, with full details reserved for the results section.
        """)

with col2:
	st.markdown("<div class='example'>**Example Results Preview**</div>", unsafe_allow_html=True)
st.markdown("""
        > Our analysis yields four main findings. First, we find that a one standard deviation increase in neighborhood exposure to foreclosures reduces house prices by 9.1 percent. Second, this effect is highly localized, with the impact declining by half for properties located more than 250 feet from the foreclosed property. Third, the price effect is persistent, remaining statistically significant for at least three years after the foreclosure. Fourth, the magnitude of the effect varies substantially across housing markets, with larger price impacts in areas with low housing supply elasticity. These findings are robust to alternative specifications, including controls for local economic conditions and spatial correlation in the error terms.
        """)

st.markdown("<div class='section-header'>Common Introduction Mistakes in Economics Papers</div>",
			unsafe_allow_html=True)

mistakes = pd.DataFrame({
    "Mistake": [
        "Vague research question",
        "Delayed contribution statement",
        "Excessive literature review",
        "Missing or unclear methodology",
        "Findings without magnitudes",
        "Overstatement of contribution",
        "Disconnected from literature"
    ],
    "Why It's Problematic": [
        "Fails to communicate specific focus and scope",
        "Risks losing reader's interest before reaching key point",
        "Dilutes focus and buries your contribution",
        "Leaves readers uncertain about empirical approach",
        "Makes it difficult to assess importance of results",
        "Damages credibility with reviewers",
        "Fails to establish relevance and incremental value"
    ],
    "Solution": [
        "State specific question in first paragraph",
        "Present contribution by second page",
        "Focus on most relevant papers and explicit gaps",
        "Clearly preview identification strategy",
        "Include specific effect sizes and statistics",
        "Make claims proportional to evidence",
        "Explicitly link your work to existing literature"
    ]
})

st.table(mistakes)


st.dataframe(mistakes, use_container_width=True)

st.markdown("<div class='section-header'>Introduction Checklist</div>", unsafe_allow_html=True)

intro_checklist = """
    <ul>
        <li><input type="checkbox"/> Research question clearly stated in first or second paragraph</li>
        <li><input type="checkbox"/> Importance of the question established (theoretical or practical)</li>
        <li><input type="checkbox"/> Relevant background or context provided</li>
        <li><input type="checkbox"/> Key literature positioned thematically with specific gaps identified</li>
        <li><input type="checkbox"/> Data sources and methodological approach previewed</li>
        <li><input type="checkbox"/> Identification strategy explained (for causal papers)</li>
        <li><input type="checkbox"/> Key findings presented with specific magnitudes</li>
        <li><input type="checkbox"/> Contribution statement explicitly articulated</li>
        <li><input type="checkbox"/> Paper roadmap included in final paragraph</li>
        <li><input type="checkbox"/> Introduction length appropriate for journal (typically 4-7 pages)</li>
    </ul>
    """

st.markdown(intro_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>Your introduction is your paper's first impression. In the competitive landscape of top economics journals, a clear, compelling introduction that efficiently communicates your research question, approach, findings, and contribution is essential for capturing editors' and reviewers' interest.</div>",
	unsafe_allow_html=True)
if selected_page == "1. Title":
    # … your code …
    pass

elif selected_page == "2. Abstract":
    # … your code …
    pass

# … other pages …

elif selected_page == "6. Literature Review":
    st.markdown(
        "<div class='sub-header'>Conducting and Writing Effective Literature Reviews</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
A thorough literature review demonstrates your command of existing research, positions your contribution 
appropriately, and convinces readers that your paper addresses an important gap. In economics, literature 
reviews must be comprehensive yet focused on establishing the context for your specific contribution.
"""
    )

    col1, col2 = create_columns(3, 2)


with col1:
	st.markdown("<div class='section-header'>Purpose and Location of Literature Reviews</div>", unsafe_allow_html=True)
st.markdown("""
        In economics papers, literature reviews serve several critical functions:

        1. **Establish intellectual context** for your research question
        2. **Demonstrate knowledge** of relevant theoretical and empirical work
        3. **Identify gaps, limitations, or contradictions** in existing research
        4. **Justify your approach** by showing how it addresses limitations
        5. **Position your contribution** within the field

        Literature review content may appear in different locations:

        - **Brief overview in introduction** (1-2 paragraphs)
        - **Dedicated literature section** following introduction (2-4 pages)
        - **Integrated throughout** theoretical or methodological sections
        - **Comparison with existing findings** in discussion section

        The appropriate structure depends on your paper's focus and the journal's conventions.
        """)

with col2:
	st.markdown("<div class='example'>**Literature Review Placement**</div>", unsafe_allow_html=True)

# Data for literature review placement
paper_types = ['Empirical', 'Theoretical', 'Methodological', 'Policy Analysis']
dedicated_section = [65, 45, 60, 70]  # percentage with dedicated lit review section
intro_only = [25, 35, 30, 20]  # percentage with lit review in intro only
integrated = [10, 20, 10, 10]  # percentage with integrated lit review

fig, ax = plt.subplots(figsize=(10, 6))

width = 0.5

ax.bar(paper_types, dedicated_section, width, label='Dedicated Section', color='steelblue')
ax.bar(paper_types, intro_only, width, bottom=dedicated_section, label='Introduction Only', color='lightsteelblue')
ax.bar(paper_types, integrated, width, bottom=[i + j for i, j in zip(dedicated_section, intro_only)],
	   label='Integrated Throughout', color='darkblue')

ax.set_ylabel('Percentage of Papers')
ax.set_title('Literature Review Placement by Paper Type in Top Economics Journals')
ax.legend()

plt.tight_layout()
st.pyplot(fig)

st.markdown("<div class='section-header'>Organizing Your Literature Review</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Effective economics literature reviews are organized thematically rather than chronologically or alphabetically. 
        Consider these organizational approaches:

        1. **Theoretical perspectives**: Group literature by competing theoretical frameworks
        2. **Methodological approaches**: Organize by empirical strategies or data sources
        3. **Key findings**: Group by results or conclusions on your research question
        4. **Evolution of understanding**: Show how knowledge has developed over time
        5. **Research dimensions**: Organize by different aspects of your topic

        Within each category, you might discuss papers chronologically to show the evolution of knowledge, 
        but the primary organization should be thematic.
        """)

with col2:
	st.markdown("<div class='example'>**Example Thematic Organization**</div>", unsafe_allow_html=True)
st.markdown("""
        From a paper on monetary policy transmission:

        > The literature on monetary policy transmission can be categorized into four main strands. First, studies on the interest rate channel examine how policy rates affect borrowing costs and investment (Bernanke and Gertler 1995; Kashyap and Stein 2000). Second, research on the credit channel focuses on financial frictions and bank lending (Kashyap et al. 1993; Jiménez et al. 2012). Third, the asset price channel literature examines effects on equity prices, housing values, and wealth (Mishkin 2007; Case et al. 2005). Finally, an emerging literature explores expectation channels and forward guidance (Campbell et al. 2012; Del Negro et al. 2015). Our paper contributes primarily to the second and fourth strands by examining how bank heterogeneity influences the transmission of policy through both traditional credit channels and expectation formation.
        """)

st.markdown("<div class='section-header'>Coverage and Depth</div>", unsafe_allow_html=True)

st.markdown("""
    One of the most challenging aspects of literature reviews is determining appropriate coverage and depth. 
    In economics, you should typically include:
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        **Essential Coverage**:

        1. **Seminal papers** that established key concepts or methods
        2. **Recent work** in top journals (last 5-10 years)
        3. **Directly competing or complementary papers**
        4. **Methodologically similar studies**
        5. **Papers addressing similar research questions**
        6. **Key literature reviews or meta-analyses**

        **Appropriate Depth**:

        - **Most papers**: Brief mention (1-2 sentences)
        - **Key papers**: More detailed discussion (3-4 sentences)
        - **Most related papers**: Extended analysis (paragraph)

        Focus on aspects of prior work most relevant to your contribution rather than 
        comprehensive summaries.
        """)

with col2:
	st.markdown(
		"<div class='tip'>💡 **Tip**: When citing multiple papers for a similar point, organize them by importance rather than alphabetically or chronologically. This signals to readers which papers you consider most relevant.</div>",
		unsafe_allow_html=True)

st.markdown(
    "<div class='caution'>⚠️ **Caution**: Avoid the \"laundry list\" approach that simply summarizes one paper after another without synthesis. This suggests a lack of critical thinking about how the literature fits together.</div>",
    unsafe_allow_html=True
)

st.markdown("<div class='example'>**Example Literature Gap Identification**</div>", unsafe_allow_html=True)
st.markdown("""
        > While this literature has advanced our understanding of minimum wage effects on employment levels, three important limitations remain. First, most studies focus on short-term employment effects, with few examining outcomes beyond a two-year window (exception: Sorkin 2015). Second, the literature has concentrated primarily on the extensive margin (employment status) rather than the intensive margin (hours worked) or other adjustments like non-wage benefits. Third, despite theoretical predictions of heterogeneous effects by firm characteristics, empirical evidence on this dimension remains sparse. Our paper addresses these three gaps by utilizing a 10-year panel, examining multiple margins of adjustment, and exploiting establishment-level data to identify differential responses by firm size and productivity.
        """)

st.markdown("<div class='section-header'>Critical Engagement vs. Summary</div>", unsafe_allow_html=True)

st.markdown("""
    A strong literature review does more than summarize previous work—it critically engages with it. 
    For each key paper or stream of research, consider:
    """)

critical_elements = pd.DataFrame({
'Element': [
	'Key findings',
	'Methodological approach',
	'Data limitations',
	'Assumptions',
	'External validity',
	'Connection to your work'
],
'Questions to Address': [
	'What were the main results? How conclusive were they?',
	'What identification strategy was used? How convincing is it?',
	'What dataset was used? What are its strengths and limitations?',
	'What theoretical or empirical assumptions underlie the analysis?',
	'To what contexts do the findings generalize?',
	'How does your paper build on, extend, or challenge this work?'
]
})

st.dataframe(critical_elements, use_container_width=True)

st.markdown("<div class='example'>**Example of Critical Engagement**</div>", unsafe_allow_html=True)
st.markdown("""
    > Card and Krueger (1994) examine the employment effects of minimum wage increases using a difference-in-differences approach comparing fast food restaurants in New Jersey and Pennsylvania. Their finding that employment did not decrease—and may have increased—following a minimum wage hike challenged conventional wisdom. However, their study has three limitations relevant to our work. First, they examine only a single industry in two states, raising questions about generalizability. Second, their short time horizon (8 months) cannot capture longer-term adjustment mechanisms. Third, their data come from telephone surveys rather than administrative sources, introducing potential measurement error. Neumark and Wascher (2000) attempt to address the third concern using payroll data, finding contrasting results, though Allegretto et al. (2017) demonstrate that methodological choices regarding control groups substantially influence conclusions. Our study advances this debate by utilizing comprehensive administrative employer-employee data covering all industries in 24 states over 12 years, allowing us to examine both short and long-run adjustments while accounting for spatial heterogeneity in employment trends.
    """)

st.markdown("<div class='section-header'>Literature Review Mistakes to Avoid</div>", unsafe_allow_html=True)

mistakes = pd.DataFrame({
    "Mistake": [
        "Excessive breadth",
        "Insufficient depth for key papers",
        "Mere summarization",
        "Missing recent work",
        "Overlooking contradictory findings",
        "Failing to identify gaps",
        "Disconnection from your contribution"
    ],
    "Why It Matters": [
        "Dilutes focus and obscures relevance to your work",
        "Suggests superficial engagement with crucial research",
        "Fails to demonstrate critical thinking and evaluation",
        "Signals you are not current with the literature",
        "Misses opportunity to highlight unresolved questions",
        "Weakens justification for your study",
        "Fails to establish how your paper advances knowledge"
    ]
})

st.table(mistakes)


st.dataframe(mistakes, use_container_width=True)

st.markdown("<div class='section-header'>Literature Review Process</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        A systematic approach to conducting literature reviews in economics:

        1. **Start broad**:
           - Search major economics journals
           - Review recent literature reviews
           - Check JEL classification

        2. **Refine systematically**:
           - Follow citations from key papers (backward search)
           - Find papers citing key works (forward search)
           - Search for specific methodologies or data

        3. **Organize findings**:
           - Create a structured database of papers
           - Categorize by theme, method, and findings
           - Identify patterns, contradictions, and gaps

        4. **Map the literature**:
           - Visualize connections between papers
           - Identify intellectual lineages
           - Locate your contribution

        5. **Synthesize**:
           - Identify major agreements and disagreements
           - Extract methodological evolution
           - Articulate specific gaps you address
        """)

with col2:
# Create a simple visualization of literature mapping
	G = nx.DiGraph()

# Add some nodes
seminal_papers = ["Paper A (1990)", "Paper B (1995)", "Paper C (1997)"]
recent_papers = ["Paper D (2015)", "Paper E (2018)", "Paper F (2020)", "Paper G (2021)", "Paper H (2022)"]
your_paper = ["Your Paper (2025)"]

# Add all nodes
for paper in seminal_papers + recent_papers + your_paper:
	G.add_node(paper)

# Add edges (connections between papers)
G.add_edge("Paper A (1990)", "Paper D (2015)")
G.add_edge("Paper A (1990)", "Paper E (2018)")
G.add_edge("Paper B (1995)", "Paper D (2015)")
G.add_edge("Paper B (1995)", "Paper F (2020)")
G.add_edge("Paper C (1997)", "Paper E (2018)")
G.add_edge("Paper C (1997)", "Paper G (2021)")
G.add_edge("Paper D (2015)", "Paper H (2022)")
G.add_edge("Paper E (2018)", "Paper H (2022)")
G.add_edge("Paper F (2020)", "Your Paper (2025)")
G.add_edge("Paper G (2021)", "Your Paper (2025)")
G.add_edge("Paper H (2022)", "Your Paper (2025)")

# Create a plot
fig, ax = plt.subplots(figsize=(8, 8))

# Position nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Draw seminal papers
nx.draw_networkx_nodes(G, pos, nodelist=seminal_papers, node_color='lightblue',
					   node_size=2000, ax=ax, alpha=0.8)

# Draw recent papers
nx.draw_networkx_nodes(G, pos, nodelist=recent_papers, node_color='lightgreen',
					   node_size=1500, ax=ax, alpha=0.8)

# Draw your paper
nx.draw_networkx_nodes(G, pos, nodelist=your_paper, node_color='red',
					   node_size=2500, ax=ax, alpha=0.8)

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, arrows=True,
					   arrowsize=15, ax=ax)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, ax=ax)

# Remove axis
ax.set_axis_off()

plt.title("Literature Mapping Example")
plt.tight_layout()
st.pyplot(fig)

st.markdown(
	"<div class='tip'>💡 **Tip**: Tools like VOSviewer, CitNetExplorer, or CiteSpace can help visualize citation networks to identify key papers and research clusters in your field.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Literature Search Resources</div>", unsafe_allow_html=True)

resources = pd.DataFrame({
'Resource': [
	'Google Scholar',
	'IDEAS/RePEc',
	'NBER Working Papers',
	'SSRN Economics Network',
	'EconLit',
	'American Economic Association Journals',
	'Journal of Economic Literature',
	'Journal of Economic Surveys',
	'Annual Review of Economics'
],
'Best For': [
	'Comprehensive search; citation tracking',
	'Economics-specific search; working papers',
	'Latest working papers from leading economists',
	'Pre-publication papers and discussion papers',
	'Curated economics publication database',
	'High-impact published research',
	'Literature reviews and surveys',
	'Thematic literature reviews',
	'Commissioned reviews of specific topics'
]
})

st.dataframe(resources, use_container_width=True)

st.markdown("<div class='section-header'>Literature Review Checklist</div>", unsafe_allow_html=True)

lit_checklist = """
    <ul>
        <li><input type="checkbox"/> Covers seminal papers in the field</li>
        <li><input type="checkbox"/> Includes recent literature (last 5-10 years)</li>
        <li><input type="checkbox"/> Organized thematically rather than chronologically</li>
        <li><input type="checkbox"/> Critically engages with methodologies and findings</li>
        <li><input type="checkbox"/> Identifies specific limitations or gaps in existing research</li>
        <li><input type="checkbox"/> Connects literature discussion directly to your contribution</li>
        <li><input type="checkbox"/> Balanced treatment of competing perspectives</li>
        <li><input type="checkbox"/> Appropriate depth for most relevant papers</li>
        <li><input type="checkbox"/> Avoids excessive breadth on tangential topics</li>
        <li><input type="checkbox"/> Synthesizes patterns and trends rather than just summarizing</li>
    </ul>
    """

st.markdown(lit_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>A strong literature review does more than demonstrate your knowledge—it strategically positions your work within the ongoing scholarly conversation. By identifying specific gaps or limitations in existing research, you create the intellectual space for your contribution.</div>",
	unsafe_allow_html=True)

if selected_page == "1. Title":
    pass

elif selected_page == "2. Abstract":
    pass

# … other pages …
elif selected_page == "7. Methodology":
    st.markdown(
        "<div class='sub-header'>Developing Robust Methodology Sections</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
The methodology section is where you establish the credibility of your research design. In economics, 
this section must demonstrate both theoretical grounding and empirical rigor, with particular attention 
to identification strategies for causal claims.
"""
    )


col1, col2 = create_columns(3, 2)

with col1:
	st.markdown("<div class='section-header'>Core Elements of Methodology Sections</div>", unsafe_allow_html=True)
st.markdown("""
        Economics methodology sections typically include these key components:

        1. **Theoretical Framework or Model**
           - Conceptual framework motivating empirical analysis
           - Formal mathematical model (where appropriate)
           - Key assumptions and their justification
           - Testable hypotheses or predictions

        2. **Data Sources and Sample Construction**
           - Origin and structure of datasets
           - Sample selection procedures and criteria
           - Time period and geographic coverage
           - Unit of observation

        3. **Variable Construction and Measurement**
           - Definitions of key variables
           - Construction of indices or composite measures
           - Summary statistics

        4. **Empirical Strategy**
           - Econometric specifications
           - Identification approach
           - Estimation procedures
           - Robustness checks
        """)

with col2:
	st.markdown("<div class='example'>**Methodology Section Length**</div>", unsafe_allow_html=True)

# Data for methodology section length
journals = ['AER', 'QJE', 'JPE', 'RESTUD', 'ECTA']
method_lengths = [6.7, 7.4, 7.1, 8.2, 8.8]  # Average methodology section length in pages

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(journals, method_lengths, color='steelblue')

ax.set_ylabel('Average Methodology Length (pages)')
ax.set_title('Methodology Section Length in Top Economics Journals')

for bar in bars:
	height = bar.get_height()
ax.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
		f'{height}', ha='center', va='bottom')

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
        **Key Takeaway**: Methodology sections in top economics journals typically constitute 20-25% of paper length, 
        with more technical journals (Econometrica, REStud) requiring more extensive methodological discussion.
        """)

st.markdown("<div class='section-header'>Theoretical Framework</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        In economics, empirical work should be guided by theoretical considerations. Your theoretical 
        framework should:

        1. **Establish causal relationships** of interest
        2. **Clarify mechanisms** connecting variables
        3. **Generate testable predictions**
        4. **Guide interpretation** of empirical results

        The appropriate depth of theoretical discussion depends on your paper's focus and contribution:

        - **Theory papers**: Extensive formal model development
        - **Applied theory**: Significant but streamlined model
        - **Empirical papers**: Conceptual framework with key equations
        - **Policy analysis**: Theory as motivation for empirical approach

        Even primarily empirical papers should articulate the theoretical basis for examined relationships.
        """)

with col2:
	st.markdown("<div class='example'>**Example Theoretical Framework (Brief)**</div>", unsafe_allow_html=True)
st.markdown("""
        From a paper on education returns:

        > We model educational investment decisions in a human capital framework based on Becker (1964) and Card (2001). Individuals maximize lifetime utility by choosing years of education, trading off current costs against future benefits. The individual's problem can be expressed as:

        > max U = Σ β^t[Y(s)·I(t≥s) - c(s)·I(t=s)]

        > where s is years of schooling, Y(s) is earnings with s years of education, c(s) is the cost of the sth year of education, β is the discount factor, and I(·) is an indicator function. The first-order condition implies that individuals invest in education until the marginal return equals the marginal cost:

        > Y'(s)/Y(s) = r + c'(s)/c(s)

        > where r is the interest rate. This framework generates three testable implications that we examine empirically: (1) returns to education are higher for individuals with lower discount rates; (2) credit constraints create a wedge between private and social returns; and (3) information frictions can lead to suboptimal investment.
        """)

st.markdown("<div class='section-header'>Data Description</div>", unsafe_allow_html=True)

st.markdown("""
    A thorough data description establishes the foundation for your empirical work. It should give readers 
    sufficient information to understand your sample and evaluate external validity.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Key elements of data description:

        1. **Data sources**
           - Origin and collection method
           - Sampling framework
           - Any linkages between datasets

        2. **Sample construction**
           - Inclusion and exclusion criteria
           - Treatment of missing values
           - Final sample size and unit of observation

        3. **Time period and geographic coverage**
           - Years covered
           - Regions or countries included
           - Any notable gaps

        4. **Key variables**
           - Precise definitions
           - Construction of derived variables
           - Units of measurement

        5. **Summary statistics**
           - Descriptive statistics of key variables
           - Comparison with population parameters when available
           - Differences across relevant subgroups
        """)

with col2:
	st.markdown("<div class='example'>**Example Summary Statistics Table**</div>", unsafe_allow_html=True)

# Create sample summary statistics table
summary_stats = pd.DataFrame({
'Variable': [
	'GDP per capita (1000s USD)',
	'Trade openness (% of GDP)',
	'Inflation rate (%)',
	'Human capital index (0-1)',
	'Institutional quality (0-10)',
	'Financial development index'
],
'Mean': [18.45, 76.32, 3.82, 0.69, 6.74, 0.57],
'Std. Dev.': [14.67, 42.56, 5.21, 0.18, 2.11, 0.25],
'Min': [0.86, 15.20, -1.40, 0.23, 1.50, 0.11],
'Max': [85.43, 210.43, 35.62, 0.92, 9.80, 0.95],
'N': [1420, 1420, 1396, 1385, 1375, 1356]
})

st.dataframe(summary_stats, use_container_width=True)

st.markdown("""
        **Good Practice Elements**:
        - Reports all key variables
        - Includes sample size for each variable
        - Shows full distribution (not just mean)
        - Clear units of measurement
        - Sufficient precision in reporting
        """)

st.markdown(
	"<div class='caution'>⚠️ **Caution**: Be transparent about data limitations, missing values, and potential selection issues. Acknowledging these upfront strengthens credibility and helps preempt reviewer concerns.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Empirical Strategy and Identification</div>", unsafe_allow_html=True)

st.markdown("""
    In economics, particular attention is paid to identification strategies that allow for causal interpretation 
    of results. This section should clearly articulate your approach to addressing potential endogeneity.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("<div class='section-header'>Common Identification Strategies</div>", unsafe_allow_html=True)
st.markdown("""
        1. **Randomized Controlled Trials (RCTs)**
           - Random assignment of treatment
           - Balance checks
           - Treatment compliance

        2. **Instrumental Variables (IV)**
           - Instrument relevance (first stage strength)
           - Exclusion restriction justification
           - Monotonicity assumption

        3. **Regression Discontinuity (RD)**
           - Running variable and cutoff justification
           - Bandwidth selection
           - Continuity of other variables at cutoff

        4. **Difference-in-Differences (DiD)**
           - Treatment and control group selection
           - Parallel trends validation
           - Event study specifications

        5. **Synthetic Control Method**
           - Donor pool selection
           - Pre-treatment fit assessment
           - Placebo tests

        6. **Fixed Effects and Panel Methods**
           - Source of identifying variation
           - Treatment of time-varying confounders
           - Selection of appropriate fixed effects
        """)

with col2:
	st.markdown("<div class='section-header'>Elements of Strong Identification Sections</div>", unsafe_allow_html=True)
st.markdown("""
        1. **Clear specification of econometric model**
           - Exact regression equations with variable definitions
           - Functional form justification
           - Error structure and clustering approach

        2. **Explicit statement of identifying assumptions**
           - Required conditions for causal interpretation
           - Theoretical and empirical support for assumptions
           - Potential threats to identification

        3. **Validation of identifying assumptions**
           - Tests of key assumptions where possible
           - Visual evidence (e.g., parallel trends plots)
           - Placebo or falsification tests

        4. **Robustness to alternative specifications**
           - Sensitivity to functional form
           - Alternative control variable sets
           - Sample restrictions

        5. **Treatment of standard errors**
           - Clustering level and justification
           - Heteroskedasticity considerations
           - Multiple hypothesis testing adjustments
        """)

st.markdown("<div class='example'>**Example Identification Strategy: Difference-in-Differences**</div>",
			unsafe_allow_html=True)
st.markdown("""
    > To identify the causal effect of minimum wage increases on employment, we implement a difference-in-differences design exploiting staggered adoption of minimum wage changes across states between 2000-2019. Our baseline specification is:

    > log(Emp)ist = β(MinWage)st + γXist + αi + δt + θs·t + εist

    > where Empist is employment at establishment i in state s at time t, MinWagest is the minimum wage in state s at time t, Xist is a vector of time-varying establishment and local labor market controls, αi are establishment fixed effects, δt are time fixed effects, and θs·t are state-specific linear time trends. The coefficient of interest, β, represents the elasticity of employment with respect to the minimum wage.

    > The key identifying assumption is that, absent minimum wage changes, employment trends would have evolved similarly in states that raised their minimum wages and those that did not, conditional on our controls. To assess this assumption, we first examine pre-treatment trends visually and through formal tests. Figure 3 shows that employment trends were indeed parallel in the three years prior to minimum wage changes. As further validation, we implement an event study specification:

    > log(Emp)ist = Σk βk·1(Time to Treatment = k)st + γXist + αi + δt + εist

    > where k indexes years relative to minimum wage changes. The coefficients βk capture the dynamic treatment effects, with β-1 normalized to zero. As shown in Figure 4, the pre-treatment coefficients are small and statistically indistinguishable from zero, supporting our identifying assumption.

    > We address two additional identification concerns. First, to account for potential policy endogeneity, we implement a border discontinuity design focusing on establishments in contiguous counties across state borders, where local economic conditions are likely similar but minimum wage policies differ. Second, to address the recent critique by Goodman-Bacon (2021) regarding staggered treatment adoption, we implement the Callaway and Sant'Anna (2021) estimator which is robust to treatment effect heterogeneity across time.
    """)

st.markdown("<div class='section-header'>Econometric Specifications</div>", unsafe_allow_html=True)

st.markdown("""
    Your econometric specifications should be presented with precise mathematical notation and clear explanation 
    of all variables and parameters.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Best practices for presenting specifications:

        1. **Use consistent mathematical notation**
        2. **Define all variables and subscripts**
        3. **Explain parameter interpretations**
        4. **Justify functional form choices**
        5. **Clarify fixed effects and clustering**
        6. **Present specifications in logical progression**
           - Baseline model
           - Main specification with full controls
           - Extensions and heterogeneity analyses

        Include both the mathematical representation and narrative explanation of your models.
        """)

with col2:
	st.markdown(
		"<div class='tip'>💡 **Tip**: When presenting multiple specifications, consider a table that shows the progression from simple to more complex models. This helps readers understand how each addition affects your results.</div>",
		unsafe_allow_html=True)

# Create specification buildup table
spec_table = pd.DataFrame({
'Variable/Feature': [
	'Treatment Variable',
	'Basic Controls',
	'Additional Controls',
	'Fixed Effects',
	'Time Trends',
	'Clustering'
],
'Model 1': [
	'✓',
	'✓',
	'',
	'State, Year',
	'',
	'State'
],
'Model 2': [
	'✓',
	'✓',
	'✓',
	'State, Year',
	'',
	'State'
],
'Model 3': [
	'✓',
	'✓',
	'✓',
	'County, Year',
	'',
	'County'
],
'Model 4 (Preferred)': [
	'✓',
	'✓',
	'✓',
	'County, Year',
	'State',
	'County'
]
})

st.dataframe(spec_table, use_container_width=True)

st.markdown("<div class='section-header'>Addressing Potential Concerns</div>", unsafe_allow_html=True)

concerns = pd.DataFrame({
'Potential Concern': [
	'Omitted variable bias',
	'Reverse causality',
	'Selection bias',
	'Measurement error',
	'External validity',
	'Multiple hypothesis testing',
	'Treatment effect heterogeneity'
],
'How to Address': [
	'Fixed effects, rich controls, bounding approaches',
	'Instrumental variables, timing strategies, natural experiments',
	'Sample selection models, bounds analysis, inverse probability weighting',
	'Instrumental variables, reliability adjustments, alternative measures',
	'Sample comparisons, subgroup analysis, representative sampling',
	'Bonferroni or Benjamini-Hochberg corrections, pre-registration',
	'Interaction terms, subgroup analysis, causal forests'
]
})

st.dataframe(concerns, use_container_width=True)

st.markdown("<div class='section-header'>Common Methodology Mistakes in Economics Papers</div>", unsafe_allow_html=True)

mistakes = pd.DataFrame({
'Mistake': [
	'Insufficient attention to identification',
	'Inadequate description of data construction',
	'Vague variable definitions',
	'Failing to address key endogeneity concerns',
	'Inadequate justification for specification choices',
	'Ignoring clustering or other error structure issues',
	'Overconfidence in instrumental variables'
],
'Why It Matters': [
	'Undermines causal interpretation of results',
	'Prevents replication and assessment of sample selection issues',
	'Creates ambiguity about what is actually being measured',
	'Leaves results open to alternative explanations',
	'Raises concerns about specification searching',
	'May substantially understate standard errors',
	'Weak or invalid instruments can create more bias than OLS'
],
'Solution': [
	'Explicitly discuss identification strategy and assumptions',
	'Provide comprehensive details on sample construction',
	'Define all variables precisely with formulas when appropriate',
	'Acknowledge endogeneity concerns and implement appropriate strategies',
	'Justify modeling choices and test robustness to alternatives',
	'Use appropriate clustering and robust standard errors',
	'Test and report instrument strength and conduct sensitivity analyses'
]
})

st.dataframe(mistakes, use_container_width=True)

st.markdown("<div class='section-header'>Methodology Checklist</div>", unsafe_allow_html=True)

method_checklist = """
    <ul>
        <li><input type="checkbox"/> Theoretical framework clearly articulated</li>
        <li><input type="checkbox"/> Data sources and sample construction fully described</li>
        <li><input type="checkbox"/> Key variables precisely defined</li>
        <li><input type="checkbox"/> Summary statistics for all important variables provided</li>
        <li><input type="checkbox"/> Econometric specifications presented with clear notation</li>
        <li><input type="checkbox"/> Identification strategy explicitly discussed</li>
        <li><input type="checkbox"/> Key identifying assumptions stated and justified</li>
        <li><input type="checkbox"/> Potential endogeneity concerns addressed</li>
        <li><input type="checkbox"/> Robustness checks described</li>
        <li><input type="checkbox"/> Treatment of standard errors and clustering explained</li>
    </ul>
    """

st.markdown(method_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>The methodology section establishes the credibility of your findings. In economics, where causal inference is often a central concern, careful attention to identification strategy and robustness is essential for publication in top journals.</div>",
	unsafe_allow_html=True)

if selected_page == "1. Title":
    pass

elif selected_page == "2. Abstract":
    pass

# … etc …
elif selected_page == "8. Results":
    st.markdown(
        "<div class='sub-header'>Presenting Results Effectively</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
The results section is the heart of your paper where you present your findings and their interpretation.
In economics, this section requires a careful balance of comprehensive reporting and focused narrative,
with particular attention to both statistical and economic significance.
"""
    )

col1, col2 = create_columns(3, 2)

with col1:
	st.markdown("<div class='section-header'>Structure of Results Sections</div>", unsafe_allow_html=True)
st.markdown("""
        An effective economics results section typically follows this structure:

        1. **Main results** (2-4 pages)
           - Baseline findings
           - Primary specification results
           - Magnitudes and economic significance

        2. **Robustness checks** (1-3 pages)
           - Alternative specifications
           - Sample restrictions
           - Sensitivity analyses

        3. **Mechanism exploration** (1-2 pages)
           - Channels of effect
           - Heterogeneity analyses
           - Mediating factors

        4. **Extensions or additional analyses** (1-2 pages)
           - Secondary outcomes
           - Long-term effects
           - Complementary findings

        Results should be presented in order of importance, not necessarily in the order analyses were conducted.
        """)

with col2:
	st.markdown("<div class='example'>**Results Section Length**</div>", unsafe_allow_html=True)

# Data for results section length
paper_types = ['Theory', 'Empirical', 'Methodological', 'Policy Analysis']
results_lengths = [3.8, 8.4, 6.2, 7.1]  # Average results section length in pages

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(paper_types, results_lengths, color='steelblue')

ax.set_ylabel('Average Results Length (pages)')
ax.set_title('Results Section Length by Paper Type')

for bar in bars:
	height = bar.get_height()
ax.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
		f'{height}', ha='center', va='bottom')

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
        **Key Takeaway**: Empirical papers have the longest results sections (25-30% of paper length), 
        while theory papers have shorter results sections as they focus more on model development.
        """)

st.markdown("<div class='section-header'>Tables and Figures</div>", unsafe_allow_html=True)

st.markdown("""
    Tables and figures are the primary vehicles for presenting your results. They should be carefully 
    designed to communicate your findings clearly and efficiently.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("<div class='section-header'>Effective Tables</div>", unsafe_allow_html=True)
st.markdown("""
        Best practices for economic research tables:

        1. **Clear, informative titles** that stand alone
        2. **Descriptive column and row headers**
        3. **Appropriate precision** in reported estimates
        4. **Standard errors** in parentheses below coefficients
        5. **Statistical significance indicators** (* for p<0.1, ** for p<0.05, *** for p<0.01)
        6. **Sample size and model fit statistics** (R², F-statistic)
        7. **Comprehensive notes** explaining variables and specifications
        8. **Logical progression** across columns (basic to comprehensive)
        9. **Comparison columns** for robustness or heterogeneity
        10. **Consistent formatting** across all tables

        Tables should be self-contained yet integrated with your narrative.
        """)

with col2:
	st.markdown("<div class='section-header'>Effective Figures</div>", unsafe_allow_html=True)
st.markdown("""
        Best practices for economic research figures:

        1. **Clear, descriptive titles**
        2. **Labeled axes** with units of measurement
        3. **Legible font sizes** for all text
        4. **Appropriate scale** to highlight patterns
        5. **Confidence intervals** or error bars where applicable
        6. **Minimal chartjunk** (unnecessary decorative elements)
        7. **Color choices** that work in grayscale
        8. **Clear legends** when multiple series appear
        9. **Source notes** for data-based figures
        10. **Consistent visual style** across figures

        Common figure types in economics:
        - Line graphs for time series
        - Scatter plots with fitted lines
        - Bar charts for comparisons
        - Event study plots
        - Coefficient plots for multiple specifications
        - Distribution plots (histograms, densities)
        """)

st.markdown("<div class='example'>**Sample Economics Results Table**</div>", unsafe_allow_html=True)

# Create sample regression results table
regression_table = pd.DataFrame({
'Variable': [
	'Treatment',
	'Log Income',
	'Education',
	'Age',
	'Female',
	'Constant',
	'',
	'Observations',
	'R-squared',
	'Controls',
	'Fixed Effects'
],
'Model 1': [
	'0.183***<br>(0.042)',
	'',
	'',
	'',
	'',
	'0.542***<br>(0.019)',
	'',
	'1,240',
	'0.114',
	'No',
	'No'
],
'Model 2': [
	'0.165***<br>(0.039)',
	'0.087**<br>(0.034)',
	'0.042**<br>(0.018)',
	'0.003<br>(0.002)',
	'-0.056<br>(0.040)',
	'0.215**<br>(0.104)',
	'',
	'1,240',
	'0.187',
	'Yes',
	'No'
],
'Model 3': [
	'0.142***<br>(0.037)',
	'0.075**<br>(0.031)',
	'0.038**<br>(0.017)',
	'0.002<br>(0.002)',
	'-0.048<br>(0.038)',
	'0.226**<br>(0.098)',
	'',
	'1,240',
	'0.276',
	'Yes',
	'Yes'
]
})

# Display the table with HTML formatting
st.markdown(
	"<table border='1' class='dataframe'><thead><tr><th>Impact of Treatment on Outcome Variable</th><th>Model 1</th><th>Model 2</th><th>Model 3</th></tr></thead>",
	unsafe_allow_html=True)

for index, row in regression_table.iterrows():
	st.markdown(
		f"<tr><td>{row['Variable']}</td><td>{row['Model 1']}</td><td>{row['Model 2']}</td><td>{row['Model 3']}</td></tr>",
		unsafe_allow_html=True)

st.markdown("</table>", unsafe_allow_html=True)
st.markdown(
	"<i>Notes: Robust standard errors in parentheses. *** p<0.01, ** p<0.05, * p<0.1. The dependent variable is the standardized outcome measure. Controls include demographic characteristics and baseline measures. Fixed effects include region and year.</i>",
	unsafe_allow_html=True)

st.markdown(
	"<div class='tip'>💡 **Tip**: In top economics journals, key results are typically presented in both tables (for precision) and figures (for visual impact). The same information can be conveyed in both formats to cater to different reader preferences.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Interpreting Coefficients</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Effective interpretation of results involves:

        1. **Technical meaning**
           - Precise interpretation of coefficients
           - Units and scaling
           - Statistical significance

        2. **Economic significance**
           - Magnitude relative to means or standard deviations
           - Comparison to relevant benchmarks
           - Practical importance

        3. **Contextual meaning**
           - Connection to theoretical predictions
           - Comparison with previous literature
           - Policy or practical implications

        Don't just report numbers—explain what they mean in the context of your research question 
        and the broader literature.
        """)

with col2:
	st.markdown("<div class='example'>**Example Coefficient Interpretation**</div>", unsafe_allow_html=True)
st.markdown("""
        Weak interpretation:
        > The coefficient on minimum wage is -0.075 and is statistically significant at the 5% level.

        Strong interpretation:
        > The coefficient of -0.075 (column 3) indicates that a 10% increase in the minimum wage is associated with a 0.75% decrease in employment. This effect is statistically significant at the 5% level. To put this magnitude in context, it implies that the average minimum wage increase in our sample period (17%) would reduce employment by approximately 1.3%. This elasticity of -0.075 is on the lower end of previous estimates, which range from -0.1 to -0.3 (Neumark and Wascher, 2010), suggesting that employment is less responsive to minimum wage changes than earlier work indicated. One explanation for this smaller magnitude is our ability to control for local economic trends through the border discontinuity design.
        """)

st.markdown("<div class='section-header'>Statistical vs. Economic Significance</div>", unsafe_allow_html=True)

st.markdown("""
    A critical distinction in economics research is between statistical significance (confidence that an effect is non-zero) 
    and economic significance (whether the effect is meaningful in magnitude). Top journals expect discussion of both.
    """)

significance_comparison = pd.DataFrame({
'Scenario': [
	'Statistically significant, economically significant',
	'Statistically significant, economically insignificant',
	'Statistically insignificant, potentially economically significant',
	'Statistically insignificant, economically insignificant'
],
'Interpretation Approach': [
	'Emphasize magnitude and precision; discuss implications',
	'Acknowledge statistical significance but explain limited practical importance',
	'Discuss potential importance but note imprecision; consider power issues',
	'Report null finding; discuss constraints on interpretation'
],
'Example Language': [
	'We find that trade liberalization increases productivity by 15% (p<0.01), a substantial effect equivalent to five years of average productivity growth.',
	'The effect is statistically significant (p<0.05) but small in magnitude—a 0.1% change representing just 1/50th of the typical annual variation.',
	'The estimated effect of 12% is economically meaningful but imprecisely estimated (p=0.14), suggesting that while important effects may exist, our design lacks statistical power to detect them with confidence.',
	'We find no evidence of an effect, with a precisely estimated null finding (effect size = -0.2%, SE = 0.3%).'
]
})

st.dataframe(significance_comparison, use_container_width=True)

st.markdown(
	"<div class='caution'>⚠️ **Caution**: Avoid the common mistake of focusing exclusively on statistical significance (p-values). Economics journals increasingly emphasize effect sizes, confidence intervals, and economic interpretation over simple binary significance testing.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Presenting Robustness Checks</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Robustness checks demonstrate that your findings are not sensitive to specific methodological choices. 
        Common approaches include:

        1. **Alternative specifications**
           - Different functional forms
           - Additional control variables
           - Alternative fixed effects structures

        2. **Sample variations**
           - Excluding outliers
           - Subperiod analysis
           - Alternative sample restrictions

        3. **Measurement alternatives**
           - Different variable definitions
           - Alternative data sources
           - Transformed variables

        4. **Estimation methods**
           - Alternative estimators
           - Different standard error calculations
           - Nonparametric approaches

        Effective robustness sections:
        - Focus on most important checks
        - Explain rationale for each check
        - Present results efficiently
        - Interpret consistency or differences
        """)

with col2:
	st.markdown("<div class='example'>**Effective Robustness Presentation**</div>", unsafe_allow_html=True)

# Create example coefficient plot for robustness checks
fig, ax = plt.subplots(figsize=(8, 6))

# Specifications and their coefficients with CIs
specs = ['Baseline', 'Alt. Controls', 'Subsample', 'Alt. Outcome', 'Alt. FE', 'Alt. Estimator']
coefs = [0.152, 0.143, 0.168, 0.137, 0.149, 0.161]
ci_low = [0.094, 0.082, 0.103, 0.065, 0.092, 0.089]
ci_high = [0.210, 0.204, 0.233, 0.209, 0.206, 0.233]

# Plot
ax.scatter(coefs, specs, s=80, color='steelblue')

# Add confidence intervals
for i, spec in enumerate(specs):
	ax.plot([ci_low[i], ci_high[i]], [spec, spec], color='steelblue', alpha=0.8)

# Add vertical line at zero
ax.axvline(x=0, color='red', linestyle='--', alpha=0.5)

ax.set_xlabel('Coefficient Estimate')
ax.set_title('Treatment Effect Across Specifications')
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
        **Effective Caption**: "Figure 4: Robustness of estimated treatment effects. This figure shows point estimates and 95% confidence intervals for our main treatment effect across different specifications. 'Baseline' is our preferred specification from Table 2, Column 3. 'Alt. Controls' adds additional demographic controls. 'Subsample' restricts to urban areas. 'Alt. Outcome' uses the alternative outcome measure. 'Alt. FE' includes industry-by-year fixed effects. 'Alt. Estimator' uses the Poisson pseudo-maximum likelihood estimator. All specifications yield qualitatively similar results."
        """)

st.markdown("<div class='section-header'>Exploring Heterogeneity and Mechanisms</div>", unsafe_allow_html=True)

st.markdown("""
    Beyond main effects, top economics papers often explore heterogeneity (how effects vary across subgroups) 
    and mechanisms (the channels through which effects operate).
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("<div class='section-header'>Heterogeneity Analysis</div>", unsafe_allow_html=True)
st.markdown("""
        Effective approaches to heterogeneity:

        1. **Theoretically motivated subgroups**
           - Base subgroups on theoretical predictions
           - Explain rationale for each comparison

        2. **Clear presentation**
           - Interaction terms or split samples
           - Visual presentation of differences
           - Statistical tests of differences

        3. **Balanced interpretation**
           - Acknowledge multiple testing concerns
           - Distinguish confirmatory from exploratory
           - Consider effect on external validity

        Common dimensions of heterogeneity:
        - Individual characteristics (income, education)
        - Institutional factors (market structure, regulations)
        - Geographic variation (urban/rural, regions)
        - Time periods (before/after policy changes)
        """)

with col2:
	st.markdown("<div class='section-header'>Mechanism Exploration</div>", unsafe_allow_html=True)
st.markdown("""
        Approaches to identifying mechanisms:

        1. **Mediation analysis**
           - Formal decompositions where appropriate
           - Sequential addition of mediating variables
           - Causal mediation techniques

        2. **Intermediate outcomes**
           - Examine outcomes along causal chain
           - Test for effects on intermediate steps
           - Compare timing of different effects

        3. **Ruling out alternatives**
           - Test predictions of alternative explanations
           - Placebo tests on unrelated outcomes
           - Timing tests for pre-treatment effects

        Clear mechanism evidence strengthens causal interpretation and enhances the theoretical contribution 
        of empirical work.
        """)

st.markdown("<div class='example'>**Example Heterogeneity Analysis**</div>", unsafe_allow_html=True)
st.markdown("""
    From a study on educational interventions:

    > Table 5 examines heterogeneity in treatment effects across student characteristics. Column 1 reproduces our main specification from Table 2. Columns 2 and 3 show results separately for students above and below the median baseline test score. The treatment effect is substantially larger for low-achieving students (0.28 SD) compared to high-achieving students (0.09 SD), with the difference statistically significant at the 1% level (p=0.002). Columns 4 and 5 split the sample by household income. The intervention is more effective for students from low-income households (0.24 SD) than high-income households (0.12 SD), though this difference is only marginally significant (p=0.073). These patterns suggest that the intervention helps close achievement gaps by benefiting disadvantaged students more.

    > To further explore heterogeneity, Figure 5 shows treatment effects across deciles of the baseline achievement distribution. The pattern reveals monotonically decreasing effects as baseline achievement increases, with the largest impacts for students in the bottom three deciles. This pattern is consistent with the theoretical prediction that students with less prior knowledge have more to gain from the structured approach of the intervention.
    """)

st.markdown("<div class='section-header'>Common Results Presentation Mistakes</div>", unsafe_allow_html=True)

mistakes = pd.DataFrame({
    "Mistake": [
        "Presenting results without interpretation",
        "Focusing only on statistical significance",
        "Overwhelming tables with too many specifications",
        "Inadequate visual presentation",
        "Selective reporting of favorable results",
        "Ignoring null findings",
        "Overinterpreting marginally significant results"
    ],
    "Why It Matters": [
        "Forces readers to draw their own conclusions",
        "Misses important discussion of magnitudes and practical significance",
        "Makes it difficult to identify key findings",
        "Misses opportunity for clear communication",
        "Raises concerns about researcher degrees of freedom",
        "Misses valuable information about what doesn't work",
        "Reduces credibility of analysis"
    ],
    "Solution": [
        "Connect each result to research question and theory",
        "Emphasize effect sizes and economic significance",
        "Focus on key specifications; move others to appendix",
        "Use figures for key relationships and comparative analyses",
        "Pre-register analyses or report all specifications",
        "Discuss null findings and their implications",
        "Be transparent about significance levels and multiple testing"
    ]
})

st.dataframe(mistakes, use_container_width=True)

st.markdown("<div class='section-header'>Results Section Checklist</div>", unsafe_allow_html=True)

results_checklist = """
    <ul>
        <li><input type="checkbox"/> Main results clearly presented with appropriate tables/figures</li>
        <li><input type="checkbox"/> Coefficients interpreted in terms of magnitude, not just significance</li>
        <li><input type="checkbox"/> Economic significance discussed alongside statistical significance</li>
        <li><input type="checkbox"/> Results connected to theoretical predictions</li>
        <li><input type="checkbox"/> Key robustness checks presented and interpreted</li>
        <li><input type="checkbox"/> Heterogeneity analyses included where appropriate</li>
        <li><input type="checkbox"/> Potential mechanisms explored</li>
        <li><input type="checkbox"/> Tables and figures properly formatted with comprehensive notes</li>
        <li><input type="checkbox"/> Narrative guides reader through key findings</li>
        <li><input type="checkbox"/> Alternative explanations considered</li>
    </ul>
    """

st.markdown(results_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>The results section is where your paper's contribution comes alive. Focus on telling a coherent, evidence-based story rather than simply reporting statistical output. Clear presentation, thoughtful interpretation, and connecting findings to theory are what distinguish exceptional economics papers from merely competent ones.</div>",
	unsafe_allow_html=True)

if selected_page == "1. Title":
    pass

elif selected_page == "2. Abstract":
    pass

# … etc …

elif selected_page == "9. Discussion":
    st.markdown(
        "<div class='sub-header'>Crafting an Insightful Discussion Section</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        """
The discussion section is where you interpret your findings in a broader context, consider their implications,
and acknowledge limitations. In economics papers, this section elevates your work beyond mere empirical findings
to meaningful contributions to knowledge.
"""
    )

col1, col2 = create_columns(3, 2)

with col1:
	st.markdown("<div class='section-header'>Purpose and Structure</div>", unsafe_allow_html=True)
st.markdown("""
        The discussion section serves several important functions:

        1. **Synthesize findings** in relation to research question
        2. **Connect empirical results to theory**
        3. **Compare with existing literature**
        4. **Address limitations** and alternative explanations
        5. **Discuss implications** for theory, policy, or practice
        6. **Suggest directions** for future research

        A well-structured discussion typically includes:

        - **Summary of key findings** (without simply repeating results)
        - **Theoretical interpretation** of results
        - **Comparison with previous literature**
        - **Implications sections** (theoretical, policy, etc.)
        - **Limitations and challenges**
        - **Future research directions**

        The discussion should be thoughtful and balanced, acknowledging both strengths and weaknesses of your approach.
        """)

with col2:
	st.markdown("<div class='example'>**Discussion Section Structure**</div>", unsafe_allow_html=True)

# Create visualization of discussion section structure
discussion_structure = {
	'Section': [
'Summary of Findings',
'Theoretical Interpretation',
'Comparison with Literature',
'Policy Implications',
'Limitations',
'Future Research'
],
'Typical Length (paragraphs)': [1, 2, 2, 2, 2, 1]
}

discussion_df = pd.DataFrame(discussion_structure)

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(discussion_df['Section'], discussion_df['Typical Length (paragraphs)'], color='steelblue')

ax.set_xlabel('Typical Length (paragraphs)')
ax.set_title('Structure of Discussion Sections in Economics Papers')

for bar in bars:
	width = bar.get_width()
ax.text(width + 0.1, bar.get_y() + bar.get_height() / 2, f'{width}',
		ha='left', va='center')

plt.tight_layout()
st.pyplot(fig)

st.markdown("<div class='section-header'>Connecting Results to Theory</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        A key element of strong economics discussions is connecting empirical findings back to theoretical frameworks. 
        This includes:

        1. **Evaluating theoretical predictions**
           - Which predictions were confirmed or contradicted?
           - How do results inform theoretical debates?
           - Do findings suggest modifications to existing theory?

        2. **Exploring mechanisms**
           - What does the evidence suggest about causal channels?
           - How do findings illuminate the "black box" of effects?
           - Are there multiple potential mechanisms at play?

        3. **Reconciling unexpected findings**
           - How can theory accommodate surprising results?
           - What extensions might explain discrepancies?
           - Are new theoretical perspectives needed?

        Avoid simplistic "results confirm theory" statements; instead, provide nuanced discussion of how 
        findings extend, refine, or challenge theoretical understandings.
        """)

with col2:
	st.markdown("<div class='example'>**Example Theoretical Discussion**</div>", unsafe_allow_html=True)
st.markdown("""
        From a paper on labor market discrimination:

        > Our findings both support and extend taste-based discrimination models. The significant wage gaps we document align with Becker's (1957) prediction that employer prejudice generates equilibrium wage differentials. However, our heterogeneity results—showing larger gaps in more concentrated markets—suggest important extensions to the theory. While Becker predicted that competition would eliminate discrimination, our findings indicate that market structure significantly moderates this effect, with monopsonistic employers retaining greater ability to discriminate.

        > Furthermore, our results on callback rates versus wage offers suggest that employers discriminate differently at different stages of the employment process. This pattern is difficult to reconcile with simple statistical discrimination models, which would predict consistent discrimination across stages based on the same underlying beliefs about productivity. Instead, our findings suggest a more complex model where employers may combine both taste-based motives and statistical inference in ways that vary across different decision points.
        """)

st.markdown("<div class='section-header'>Comparison with Existing Literature</div>", unsafe_allow_html=True)

st.markdown("""
    Placing your findings in the context of existing research is essential. This involves:
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        1. **Points of agreement**
           - Where do your findings reinforce existing knowledge?
           - How do they provide additional support for established theories?
           - What previous findings do you replicate or extend?

        2. **Points of difference**
           - Where do your findings contradict previous work?
           - What methodological differences might explain discrepancies?
           - How do context or sample differences matter?

        3. **Novel contributions**
           - What new insights does your work add?
           - How do you extend the scope of previous findings?
           - What questions do you answer that previous work couldn't?

        The goal is to position your work within the ongoing scholarly conversation—building on 
        some aspects while challenging or extending others.
        """)

with col2:
	st.markdown(
		"<div class='tip'>💡 **Tip**: Create a comparison table between your findings and key prior studies. This helps readers quickly grasp how your work relates to the literature and highlights your distinctive contribution.</div>",
		unsafe_allow_html=True)

# Create literature comparison table
comparison_table = pd.DataFrame({
'Study': [
	'Smith et al. (2018)',
	'Johnson (2020)',
	'Wong & Lee (2019)',
	'Current Study'
],
'Sample': [
	'US firms, 1990-2010',
	'European firms, 2005-2015',
	'Global sample, 2000-2015',
	'US and Europe, 1995-2020'
],
'Main Finding': [
	'Effect = 0.21',
	'Effect = 0.15',
	'Effect = 0.08',
	'Effect = 0.17'
],
'Key Difference': [
	'No causal identification',
	'Limited to listed firms',
	'Aggregated data only',
	'Granular data with causal design'
]
})

st.dataframe(comparison_table, use_container_width=True)

st.markdown("<div class='section-header'>Addressing Limitations</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Acknowledging limitations is a mark of scientific integrity and preempts reviewer criticism. 
        Effective discussions of limitations:

        1. **Identify key constraints** on interpretation
           - Data limitations
           - Methodological challenges
           - External validity concerns

        2. **Assess impact on conclusions**
           - How might limitations affect the interpretation of findings?
           - Which results are most/least robust to these concerns?
           - What direction of bias is likely?

        3. **Describe mitigation strategies**
           - What steps did you take to address limitations?
           - What robustness checks help alleviate concerns?
           - When are limitations most/least problematic?

        Be forthright about limitations, but avoid undermining your contribution with excessive hedging. 
        Focus on reasonable limitations that readers should consider when interpreting your findings.
        """)

with col2:
	st.markdown("<div class='example'>**Example Limitations Discussion**</div>", unsafe_allow_html=True)
st.markdown("""
        > Our study has three important limitations. First, while our identification strategy leverages quasi-random variation in policy implementation, we cannot completely rule out the possibility that unobserved local economic trends correlate with policy timing. We address this concern by including region-specific time trends and conducting extensive placebo tests, but some caution is warranted in causal interpretation.

        > Second, our data cover only formal sector employment, which represents approximately 65% of the labor force in our context. Effects may differ in the informal sector, where minimum wage enforcement is weaker and workers are typically more vulnerable. This limitation affects the generalizability of our findings to the entire labor market.

        > Third, our analysis examines short to medium-term effects (up to three years post-implementation), but longer-term adjustment mechanisms, such as automation or business relocation, may generate different patterns over extended time horizons. Future research with longer panels would be valuable for examining these dynamics.
        """)

st.markdown(
	"<div class='caution'>⚠️ **Caution**: Avoid introducing major limitations that fundamentally undermine your findings. If such significant limitations exist, they should be addressed in your research design rather than simply acknowledged in discussion.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Policy and Practical Implications</div>", unsafe_allow_html=True)

st.markdown("""
    Many economics papers include discussion of policy implications. These should be:
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        1. **Grounded in evidence**
           - Derive implications directly from your findings
           - Distinguish between strong and tentative implications
           - Acknowledge context-dependence

        2. **Appropriately qualified**
           - Clarify when moving beyond direct evidence
           - Acknowledge implementation challenges
           - Consider potential unintended consequences

        3. **Specific and actionable**
           - Provide concrete policy recommendations when justified
           - Consider implications for different stakeholders
           - Suggest how findings might inform policy design

        The strength of policy implications should be proportional to the strength and generalizability 
        of your evidence. Avoid overreaching beyond what your findings can support.
        """)

with col2:
	st.markdown("<div class='example'>**Example Policy Implications**</div>", unsafe_allow_html=True)
st.markdown("""
        Weak policy discussion:
        > Our findings have important policy implications. Policymakers should consider these results when designing future interventions.

        Strong policy discussion:
        > Our findings have three specific implications for education policy. First, the heterogeneous effects we document suggest that targeted tutoring programs would be most cost-effective if focused on students in the bottom quartile of baseline achievement, where effects are 3.2 times larger than for students above the median. Second, the timing results indicate that intervention before grade 4 produces substantially larger effects, suggesting early implementation is crucial. Third, our cost-effectiveness comparison ($150 per 0.1 standard deviation improvement) compares favorably to alternative interventions such as class size reduction ($400 per 0.1 SD) and teacher professional development ($250 per 0.1 SD), suggesting reallocation of resources toward this approach could improve overall outcomes within existing budget constraints.
        """)

st.markdown("<div class='section-header'>Future Research Directions</div>", unsafe_allow_html=True)

st.markdown("""
    Suggesting future research directions demonstrates your understanding of how your work contributes to 
    the broader research agenda.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Effective future research suggestions:

        1. **Address current limitations**
           - How might future work overcome constraints?
           - What data or methods would strengthen conclusions?

        2. **Extend findings to new contexts**
           - What other settings could test generalizability?
           - Which populations merit examination?

        3. **Explore mechanisms further**
           - How could causal channels be better isolated?
           - What intermediary outcomes could be measured?

        4. **Connect to related questions**
           - What logical next questions emerge?
           - How might findings inform adjacent research areas?

        Be specific rather than generic, and focus on the most promising directions 
        rather than providing an exhaustive list.
        """)

with col2:
	st.markdown("<div class='example'>**Example Future Research Directions**</div>", unsafe_allow_html=True)
st.markdown("""
        Generic approach:
        > Future research should further explore these questions with more data and in different contexts.

        Specific approach:
        > Our findings suggest three promising directions for future research. First, extending the analysis to countries with different institutional environments would help clarify how labor market regulations moderate the effects we document. The contrasting regulatory frameworks in Scandinavian versus Mediterranean European countries offer a potentially illuminating comparison. Second, our inability to directly observe firm decision-making processes suggests that complementary qualitative research, perhaps using executive interviews or surveys, could help unpack the "black box" of how firms implement adjustment strategies. Finally, longer-term analysis would be valuable, as our five-year window may not capture full adjustment dynamics, particularly for capital-intensive industries where investment cycles exceed our time frame.
        """)

st.markdown("<div class='section-header'>Common Discussion Section Mistakes</div>", unsafe_allow_html=True)

mistakes = pd.DataFrame({
'Mistake': [
	'Simply restating results',
	'Overinterpreting findings',
	'Introducing new results',
	'Ignoring contradictory literature',
	'Inadequate limitations discussion',
	'Unfounded policy implications',
	'Generic future research suggestions'
],
'Why It Matters': [
	'Misses opportunity to add value beyond results reporting',
	'Reduces credibility and may mislead readers',
	'Confuses readers and violates paper structure conventions',
	'Fails to position work in full intellectual context',
	'Appears unaware of research constraints',
	'May lead to inappropriate practical applications',
	'Demonstrates lack of insight into research frontier'
],
'Solution': [
	'Focus on interpretation and implications, not repetition',
	'Maintain balance between significance and constraints',
	'Keep new findings for results section or future papers',
	'Engage with conflicting findings and explain differences',
	'Acknowledge key limitations transparently',
	'Ground policy suggestions directly in evidence',
	'Provide specific, concrete research suggestions'
]
})

st.dataframe(mistakes, use_container_width=True)

st.markdown("<div class='section-header'>Discussion Section Checklist</div>", unsafe_allow_html=True)

discussion_checklist = """
    <ul>
        <li><input type="checkbox"/> Summary of key findings without merely repeating results</li>
        <li><input type="checkbox"/> Connection of empirical results to theoretical framework</li>
        <li><input type="checkbox"/> Comparison with previous literature, noting agreements and differences</li>
        <li><input type="checkbox"/> Honest discussion of limitations and their implications</li>
        <li><input type="checkbox"/> Well-justified policy or practical implications</li>
        <li><input type="checkbox"/> Specific suggestions for future research</li>
        <li><input type="checkbox"/> Balanced tone that acknowledges both strengths and constraints</li>
        <li><input type="checkbox"/> No introduction of new results</li>
        <li><input type="checkbox"/> Appropriate emphasis on most important implications</li>
        <li><input type="checkbox"/> Clear connection to original research question</li>
    </ul>
    """

st.markdown(discussion_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>The discussion section is your opportunity to demonstrate scholarly depth and connect your specific findings to broader economic understanding. Done well, it transforms a competent empirical exercise into a meaningful contribution to economic knowledge.</div>",
	unsafe_allow_html=True)

if selected_page == "1. Title":
    # … your code …
    pass

elif selected_page == "2. Abstract":
    # … your code …
    pass

# … other pages …
elif selected_page == "10. Conclusion":
    st.markdown(
        "<div class='sub-header'>Writing Effective Conclusions</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
The conclusion provides closure to your paper, reinforcing key points and leaving readers with a clear understanding
of your contribution. While relatively brief, a well-crafted conclusion significantly impacts how readers remember
your work.
"""
    )


col1, col2 = create_columns(3, 2)

with col1:
	st.markdown("<div class='section-header'>Purpose and Structure</div>", unsafe_allow_html=True)
st.markdown("""
        The conclusion section serves several important functions:

        1. **Synthesize the paper's key elements**
        2. **Reinforce the main contribution**
        3. **Leave readers with a clear takeaway message**
        4. **Frame the work's significance**

        Effective economics paper conclusions typically follow this structure:

        - **Brief restatement of research question** (1 sentence)
        - **Concise summary of approach** (1-2 sentences)
        - **Key findings recap** (2-3 sentences)
        - **Main contribution emphasized** (1-2 sentences)
        - **Broader significance or implications** (1-2 sentences)
        - **Final thought or takeaway** (1 sentence)

        Conclusions are typically 1-2 paragraphs (or about 1 page) in top economics journals.
        """)

with col2:
	st.markdown("<div class='example'>**Conclusion Length**</div>", unsafe_allow_html=True)

# Data for conclusion length
journals = ['American Economic Review', 'Quarterly Journal of Economics',
			'Journal of Political Economy', 'Econometrica', 'Review of Economic Studies']
lengths = [1.1, 1.3, 0.9, 0.8, 1.0]  # Average conclusion length in pages

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(journals, lengths, color='steelblue')

ax.set_ylabel('Average Conclusion Length (pages)')
ax.set_title('Conclusion Length in Top Economics Journals')
ax.set_xticklabels(journals, rotation=45, ha='right')

for bar in bars:
	height = bar.get_height()
ax.text(bar.get_x() + bar.get_width() / 2., height + 0.05,
		f'{height}', ha='center', va='bottom')

plt.tight_layout()
st.pyplot(fig)

st.markdown("<div class='section-header'>What to Include in Conclusions</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("<div class='section-header'>Essential Elements</div>", unsafe_allow_html=True)
st.markdown("""
        1. **Research question recap**
           - Briefly restate the central question
           - Remind readers of the puzzle or motivation

        2. **Approach summary**
           - Concisely mention methodology
           - Reference key data or identification strategy

        3. **Main findings**
           - Highlight 2-3 most important results
           - Include specific magnitudes for key effects

        4. **Contribution statement**
           - Explicitly state how paper advances literature
           - Emphasize what's novel or distinctive

        5. **Significance framework**
           - Connect to broader economic questions
           - Note theoretical or policy relevance
        """)

with col2:
	st.markdown("<div class='section-header'>What to Avoid</div>", unsafe_allow_html=True)
st.markdown("""
        1. **New information**
           - No new results or analyses
           - No new literature citations

        2. **Excessive detail**
           - Not every finding needs mention
           - Avoid technical details

        3. **Overqualification**
           - Limitations already addressed in discussion
           - Avoid undermining your contribution

        4. **Generic statements**
           - "More research is needed"
           - "This is an important topic"

        5. **Abrupt endings**
           - Don't end with minor points
           - Avoid ending with limitations
        """)

st.markdown("<div class='section-header'>Conclusion Templates</div>", unsafe_allow_html=True)

with st.expander("Template 1: Empirical Paper Conclusion"):
	st.markdown("""
        ```
        This paper examined [research question] using [data/methodology approach]. 
        We find that [key finding 1 with specific magnitude] and [key finding 2 with specific magnitude]. 
        These results [support/challenge] the view that [theoretical perspective] and contribute to the literature by [specific contribution]. 
        Our findings have implications for [policy area or economic understanding], suggesting that [specific implication].
        ```

        **Example**:

        > This paper examined how financial deregulation affects small business lending and entrepreneurship using branch-level data from the banking deregulation wave of the 1990s. We find that interstate banking deregulation increased small business lending by 17% and new business formation by 8% in affected markets. These results support the view that credit constraints significantly impact entrepreneurial activity and contribute to the literature by establishing a causal link between banking competition and business dynamism. Our findings have implications for current debates on banking regulation, suggesting that policies promoting competition in local banking markets may stimulate entrepreneurship and economic growth.
        """)

with st.expander("Template 2: Theoretical Paper Conclusion"):
	st.markdown("""
        ```
        This paper developed a [type of model] to analyze [economic phenomenon]. 
        The model demonstrates that [key theoretical result] under conditions of [key assumptions]. 
        This framework helps explain [empirical puzzle] and extends existing theory by [specific contribution]. 
        These results suggest [broader theoretical or policy implications] and highlight the importance of [key economic mechanism].
        ```

        **Example**:

        > This paper developed a dynamic general equilibrium model to analyze skill-biased technological change in open economies. The model demonstrates that trade liberalization amplifies the wage effects of technological change under conditions of imperfect labor mobility and complementarity between imported inputs and skilled labor. This framework helps explain the simultaneous increase in trade volumes and skill premiums observed in both developed and developing countries and extends existing theory by incorporating realistic frictions in labor market adjustment. These results suggest that trade and technology should be viewed as complementary rather than competing explanations for rising inequality and highlight the importance of transition policies that facilitate worker reallocation across sectors.
        """)

with st.expander("Template 3: Policy Analysis Conclusion"):
	st.markdown("""
        ```
        This paper evaluated [policy intervention] using [methodological approach]. 
        Our analysis shows that the policy [increased/decreased] [outcome] by [magnitude], with [heterogeneity finding]. 
        These findings contribute to the ongoing debate about [policy area] by [specific contribution]. 
        The results suggest that [policy recommendation] would be more effective for achieving [policy goal].
        ```

        **Example**:

        > This paper evaluated the impact of earned income tax credit (EITC) expansions using administrative tax data and a regression discontinuity design. Our analysis shows that the 2009 EITC expansion increased labor force participation by 2.1 percentage points among single mothers, with substantially larger effects (4.3 percentage points) for those with less than a high school education. These findings contribute to the ongoing debate about optimal income support policies by demonstrating that well-designed work incentives can simultaneously reduce poverty and increase employment. The results suggest that further expanding the EITC for workers without dependent children would be more effective for addressing poverty among this population than alternative proposals that lack employment incentives.
        """)

st.markdown("<div class='example'>**Example of an Effective Conclusion**</div>", unsafe_allow_html=True)
st.markdown("""
    From "The Returns to Hospital Consolidation" (hypothetical example):

    > This paper investigated how hospital mergers affect prices, quality, and access to care using detailed administrative data on hospital claims and patient outcomes from 2005-2022. Leveraging a difference-in-differences design with matched control markets, we find that hospital consolidation increases prices by 17% on average while reducing measures of care quality by 8% and leaving access largely unchanged. Examining heterogeneity across markets, we show that price effects are substantially larger (28%) in markets with limited insurer competition, suggesting that countervailing power plays an important role in determining merger outcomes. These findings contribute to both the industrial organization literature on healthcare markets and ongoing policy debates about antitrust enforcement. Our results indicate that current merger review processes may be insufficient to protect consumer welfare in healthcare markets, particularly in regions with concentrated insurance markets. More broadly, this study highlights how market structure interacts with the unique features of healthcare to determine economic outcomes in this vital sector.
    """)

st.markdown(
	"<div class='caution'>⚠️ **Caution**: Avoid ending your paper with limitations, caveats, or calls for future research. While these elements belong in the discussion section, the conclusion should leave readers with a strong impression of your contribution and its significance.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Crafting a Memorable Final Sentence</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        The final sentence of your paper is particularly important for creating a lasting impression. 
        Effective closing sentences often:

        1. **Emphasize broader significance**
           - Connect to fundamental economic questions
           - Note implications beyond immediate findings

        2. **Highlight key insight**
           - Distill the central lesson or takeaway
           - Capture the essential contribution

        3. **Frame future perspective**
           - Suggest how the field might evolve
           - Indicate new directions opened by your work

        4. **Connect to opening motivation**
           - Create narrative closure by returning to initial motivation
           - Show how paper addressed initial puzzle

        Avoid ending with minor points, technical details, or qualifications.
        """)

with col2:
	st.markdown("<div class='example'>**Example Closing Sentences**</div>", unsafe_allow_html=True)
st.markdown("""
        **Emphasizing broader significance**:
        > These findings underscore the fundamental role of information frictions in shaping labor market outcomes, even in the digital age of seemingly abundant information.

        **Highlighting key insight**:
        > Our results reveal that when institutions are weak, increased resource wealth can paradoxically reduce long-term economic welfare despite short-term consumption gains.

        **Framing future perspective**:
        > As economies increasingly digitize, the mechanisms we identify suggest both opportunities for reducing inequality and risks of further divergence, depending on policy choices that influence technology adoption.

        **Connecting to opening motivation**:
        > Returning to the puzzle that motivated this study, we find that the inflation-output tradeoff remains a central feature of monetary policy, but its slope varies substantially with the transparency and credibility of central bank communications.
        """)

st.markdown("<div class='section-header'>Common Conclusion Mistakes</div>", unsafe_allow_html=True)

mistakes = pd.DataFrame({
    "Mistake": [
        "Exact repetition of abstract",
        "Introducing new material",
        "Excessive hedging of findings",
        "Ending with limitations",
        "Generic statements",
        "Overly long or detailed",
        "Abrupt ending"
    ],
    "Why It Matters": [
        "Misses opportunity to reinforce key messages differently",
        "Confuses readers and violates paper structure",
        "Undermines the significance of contribution",
        "Creates negative final impression",
        "Fails to distinguish your specific contribution",
        "Dilutes impact of key points",
        "Leaves readers without closure"
    ],
    "Solution": [
        "Restate key points with fresh language and emphasis",
        "Keep new content for future papers",
        "Acknowledge limitations in discussion, emphasize strengths in conclusion",
        "End with significance or implications",
        "Make specific statements about your paper's contribution",
        "Focus on 2-3 most important points only",
        "Craft deliberate closing sentence with broader significance"
    ]
})

st.dataframe(mistakes, use_container_width=True)

st.markdown("<div class='section-header'>Conclusion Checklist</div>", unsafe_allow_html=True)

conclusion_checklist = """
    <ul>
        <li><input type="checkbox"/> Brief restatement of research question</li>
        <li><input type="checkbox"/> Concise mention of methodological approach</li>
        <li><input type="checkbox"/> Summary of 2-3 key findings with specific magnitudes</li>
        <li><input type="checkbox"/> Clear statement of main contribution</li>
        <li><input type="checkbox"/> Indication of broader significance or implications</li>
        <li><input type="checkbox"/> Strong closing sentence with lasting impression</li>
        <li><input type="checkbox"/> Appropriate length (typically 1-2 paragraphs)</li>
        <li><input type="checkbox"/> No new information or analyses</li>
        <li><input type="checkbox"/> No excessive detail or technical aspects</li>
        <li><input type="checkbox"/> No ending with limitations or hedging</li>
    </ul>
    """

st.markdown(conclusion_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>Your conclusion is the last impression readers will have of your paper. A concise, powerful conclusion reinforces your key findings and contribution, leaving readers with a clear understanding of why your paper matters.</div>",
	unsafe_allow_html=True)

# Page 11: References & Citations


if selected_page == "1. Title":
    pass

elif selected_page == "2. Abstract":
    pass

# … etc …
elif selected_page == "11. References & Citations":
    st.markdown(
        "<div class='sub-header'>Managing References and Citations</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
Proper citation is essential in academic economics papers. It acknowledges intellectual debts, 
helps readers locate relevant literature, and establishes your credibility as a researcher who 
is familiar with the field.
"""
    )


col1, col2 = create_columns(3, 2)

with col1:
	st.markdown("<div class='section-header'>Citation Styles in Economics</div>", unsafe_allow_html=True)
st.markdown("""
        Economics journals typically use author-date citation styles, with some variation across publications. 
        The most common styles are:

        1. **American Economic Association (AEA) style**
           - Used by AER, AEJ series, JEL, etc.
           - Author-date citations in parentheses
           - Alphabetical reference list

        2. **Chicago Author-Date style**
           - Used by Journal of Political Economy and others
           - Similar to AEA style with minor formatting differences

        3. **Harvard style**
           - Used by various economics journals
           - Author-date citations with specific formatting

        4. **Journal-specific styles**
           - Some journals have unique formatting requirements
           - Always check the specific journal guidelines

        Most economics papers use in-text citations in parentheses (e.g., Smith 2020) rather than footnotes or 
        endnotes for references, though footnotes may be used for supplementary information.
        """)

with col2:
	st.markdown("<div class='example'>**Citation Style Comparison**</div>", unsafe_allow_html=True)

# Create table with citation style examples
citation_styles = pd.DataFrame({
'Style': [
	'AEA',
	'Chicago Author-Date',
	'Harvard',
	'Quarterly Journal of Economics'
],
'In-Text Citation Example': [
	'(Acemoglu and Robinson 2012)',
	'(Acemoglu and Robinson 2012)',
	'(Acemoglu & Robinson, 2012)',
	'(Acemoglu and Robinson, 2012)'
],
'Multiple Works Example': [
	'(Smith 2005, 2010; Jones 2015)',
	'(Smith 2005, 2010; Jones 2015)',
	'(Smith, 2005, 2010; Jones, 2015)',
	'(Smith, 2005, 2010; Jones, 2015)'
]
})

st.dataframe(citation_styles, use_container_width=True)

st.markdown("<div class='section-header'>Reference Management Tools</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Using reference management software can significantly streamline the citation process:

        1. **Popular tools for economists**:
           - **Zotero**: Free, open-source, with browser integration
           - **Mendeley**: Free with PDF management features
           - **EndNote**: Comprehensive but paid solution
           - **BibTeX/JabRef**: Popular with LaTeX users

        2. **Key features to look for**:
           - Citation style selection (including economics styles)
           - PDF organization and annotation
           - Browser integration for easy capturing
           - Word processor integration
           - Collaboration capabilities

        3. **Best practices**:
           - Organize references with consistent tagging
           - Add detailed metadata when importing
           - Back up your reference library regularly
           - Use folders for different projects
           - Include DOIs and permanent links when available
        """)

with col2:
# Create comparison of reference managers
	ref_managers = pd.DataFrame({
'Feature': [
	'Cost',
	'Economics styles',
	'PDF management',
	'MS Word integration',
	'LaTeX support',
	'Browser extension',
	'Cloud sync',
	'Collaboration'
],
'Zotero': [
	'Free',
	'Excellent',
	'Good',
	'Yes',
	'Yes',
	'Yes',
	'Limited free',
	'Yes'
],
'Mendeley': [
	'Free',
	'Good',
	'Excellent',
	'Yes',
	'Yes',
	'Yes',
	'Yes',
	'Limited'
],
'EndNote': [
	'Paid',
	'Excellent',
	'Excellent',
	'Excellent',
	'Limited',
	'Yes',
	'Yes',
	'Limited'
],
'JabRef/BibTeX': [
	'Free',
	'Good',
	'Basic',
	'Limited',
	'Excellent',
	'Limited',
	'No',
	'No'
]
})

st.dataframe(ref_managers, use_container_width=True)

st.markdown(
	"<div class='tip'>💡 **Tip**: Most economics journals accept LaTeX submissions, which handles citations elegantly through BibTeX. For complex papers with many mathematical expressions and references, LaTeX is often preferred over Word.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>AEA Style Reference Examples</div>", unsafe_allow_html=True)

with st.expander("Journal Article"):
	st.markdown("""
        **Format**:
        ```
        Author, First Name, and First Name Last Name. Year. "Article Title." Journal Name Volume (Issue): Page range.
        ```

        **Example**:
        ```
        Acemoglu, Daron, and James A. Robinson. 2008. "Persistence of Power, Elites, and Institutions." American Economic Review 98 (1): 267-93.
        ```

        **In-text citation**:
        - Single author: (Smith 2020)
        - Two authors: (Acemoglu and Robinson 2008)
        - Three or more authors: (Banerjee et al. 2015)

        **Multiple works by same author**:
        - Different years: (Smith 2018, 2020)
        - Same year: (Smith 2020a, 2020b)
        """)

with st.expander("Book"):
	st.markdown("""
        **Format**:
        ```
        Author, First Name. Year. Book Title. Edition. City: Publisher.
        ```

        **Example**:
        ```
        Acemoglu, Daron, and James A. Robinson. 2012. Why Nations Fail: The Origins of Power, Prosperity, and Poverty. New York: Crown Business.
        ```

        **Book chapter**:
        ```
        Autor, David H. 2014. "Skills, Education, and the Rise of Earnings Inequality among the Other 99 Percent." In Science 344 (6186): 843-51.
        ```
        """)

with st.expander("Working Paper"):
	st.markdown("""
        **Format**:
        ```
        Author, First Name. Year. "Paper Title." Working Paper Series Name Working Paper Number, Institution.
        ```

        **Example**:
        ```
        Chetty, Raj, Nathaniel Hendren, Patrick Kline, and Emmanuel Saez. 2014. "Where is the Land of Opportunity? The Geography of Intergenerational Mobility in the United States." NBER Working Paper 19843, National Bureau of Economic Research.
        ```
        """)

with st.expander("Online Source"):
	st.markdown("""
        **Format**:
        ```
        Author, First Name. Year. "Title." Publisher or Website. Access date. URL.
        ```

        **Example**:
        ```
        Federal Reserve Bank of St. Louis. 2020. "Federal Debt: Total Public Debt as Percent of Gross Domestic Product." FRED Economic Data. Accessed September 15, 2020. https://fred.stlouisfed.org/series/GFDEGDQ188S.
        ```
        """)

st.markdown("<div class='section-header'>Citation Best Practices in Economics</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        1. **What to cite**:
           - Theoretical concepts and models
           - Empirical findings
           - Methodological approaches
           - Data sources
           - Direct quotations (used sparingly)

        2. **Strategic citation**:
           - Cite the original source for concepts
           - Include recent applications
           - Balance classic and recent literature
           - Cite top journals when possible
           - Include relevant work from your target journal

        3. **Citation depth**:
           - General knowledge needs no citation
           - Specific findings or arguments need citation
           - Multiple citations for well-established facts
           - Single citations for specific studies

        4. **Citation placement**:
           - Place citations where claims are first made
           - Avoid redundant citations for the same point
           - Group related citations in parentheses
           - Order multiple citations alphabetically or by relevance
        """)

with col2:
	st.markdown("<div class='caution'>⚠️ **Caution**: Avoid these common citation mistakes:</div>",
				unsafe_allow_html=True)
st.markdown("""
        1. **Citation dumping**: Listing many references without clear purpose
        2. **Missing original sources**: Citing secondary sources instead of original works
        3. **Self-citation overuse**: Excessive citation of your own work
        4. **Citation-claim mismatch**: Cited paper doesn't support the claim made
        5. **Outdated references**: Relying on older literature when newer work exists
        6. **Missing influential papers**: Overlooking key contributions in your field
        7. **Inconsistent formatting**: Mixing citation styles within a paper
        """)

st.markdown("<div class='example'>**Example of Effective Citations**</div>", unsafe_allow_html=True)
st.markdown("""
        > The impact of minimum wages on employment remains contested. Early studies found negative employment effects (Brown et al. 1982; Neumark and Wascher 1992), while more recent work using border discontinuity designs has found minimal employment impacts (Card and Krueger 1994; Dube et al. 2010). Recent theoretical work suggests that these disparate findings might be reconciled by accounting for labor market frictions (Manning 2021) and firm heterogeneity (Dustmann et al. 2022).
        """)

st.markdown("<div class='section-header'>Reference List Organization</div>", unsafe_allow_html=True)

st.markdown("""
    Proper organization of the reference list is essential for reader navigation and journal compliance:
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        1. **Ordering**:
           - Alphabetical by first author's last name
           - Multiple works by same author chronologically
           - Same-year publications with a, b, c suffixes

        2. **Formatting**:
           - Hanging indentation for readability
           - Consistent punctuation throughout
           - Author names in consistent format
           - Journal names typically not abbreviated

        3. **Completeness**:
           - Include all cited works
           - Provide complete publication information
           - Include DOIs when available
           - For forthcoming articles, use "forthcoming" instead of year

        4. **Online sources**:
           - Include access dates
           - Use permanent links when possible
           - Specify type of online document
        """)

with col2:
	st.markdown(
		"<div class='tip'>💡 **Tip**: Double-check for consistency between in-text citations and the reference list. Common errors include missing references, mismatched years, and name spelling variations.</div>",
		unsafe_allow_html=True)

st.markdown("<div class='example'>**Example Reference List Section**</div>", unsafe_allow_html=True)
st.markdown("""
        **References**

        Acemoglu, Daron, and James A. Robinson. 2012. Why Nations Fail: The Origins of Power, Prosperity, and Poverty. New York: Crown Business.

        Angrist, Joshua D., and Jörn-Steffen Pischke. 2009. Mostly Harmless Econometrics: An Empiricist's Companion. Princeton: Princeton University Press.

        Card, David. 1999. "The Causal Effect of Education on Earnings." In Handbook of Labor Economics, Vol. 3A, edited by Orley Ashenfelter and David Card, 1801-63. Amsterdam: Elsevier.

        Card, David, and Alan B. Krueger. 1994. "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania." American Economic Review 84 (4): 772-93.

        Chetty, Raj, Nathaniel Hendren, Patrick Kline, and Emmanuel Saez. 2014. "Where is the Land of Opportunity? The Geography of Intergenerational Mobility in the United States." Quarterly Journal of Economics 129 (4): 1553-1623.

        Duflo, Esther, Pascaline Dupas, and Michael Kremer. 2015. "Education, HIV, and Early Fertility: Experimental Evidence from Kenya." American Economic Review 105 (9): 2757-97.
        """)

st.markdown("<div class='section-header'>Data Citation</div>", unsafe_allow_html=True)

st.markdown("""
    Economics journals increasingly require formal citation of datasets. Proper data citation includes:
    """)

data_citation = pd.DataFrame({
'Element': [
	'Creator/Author',
	'Year of publication',
	'Dataset title',
	'Repository/Archive/Publisher',
	'Version/Edition',
	'Access information',
	'DOI or URL'
],
'Example': [
	'U.S. Bureau of Labor Statistics',
	'2022',
	'Current Population Survey',
	'IPUMS',
	'Annual Social and Economic Supplement, 2022',
	'Accessed March 15, 2023',
	'https://doi.org/10.18128/D030.V9.0'
]
})

st.dataframe(data_citation, use_container_width=True)

st.markdown("<div class='example'>**Example Data Citation**</div>", unsafe_allow_html=True)
st.markdown("""
    For AEA style:

    ```
    Flood, Sarah, Miriam King, Renae Rodgers, Steven Ruggles, J. Robert Warren, and Michael Westberry. 2022. "Integrated Public Use Microdata Series, Current Population Survey: Version 10.0 [dataset]." Minneapolis, MN: IPUMS. https://doi.org/10.18128/D030.V10.0.
    ```

    In-text citation:
    ```
    Data from the Current Population Survey (Flood et al. 2022) show...
    ```
    """)

st.markdown("<div class='section-header'>Code Citation and Availability</div>", unsafe_allow_html=True)

st.markdown("""
    Many economics journals now require code and data availability for replication. Best practices include:
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        1. **Code availability statement**:
           - Where code is available (repository, journal supplement)
           - Any access restrictions
           - Software and version requirements

        2. **Code citation**:
           - Cite distinctive code or algorithms used
           - Reference software packages with specific versions
           - Include both in-text citation and reference entry

        3. **Repository options**:
           - Journal supplementary materials
           - Harvard Dataverse
           - OpenICPSR
           - GitHub (with permanent link)
           - Zenodo
        """)

with col2:
	st.markdown("<div class='example'>**Example Code Availability Statement**</div>", unsafe_allow_html=True)
st.markdown("""
        > Replication files: The data and code required to reproduce all results in this paper are available in the American Economic Association Data and Code Repository: https://doi.org/10.1257/aer.20180992.data.
        """)

st.markdown("<div class='example'>**Example Software Citation**</div>", unsafe_allow_html=True)
st.markdown("""
        > The analysis was conducted using Stata version 17.0 (StataCorp 2021) and R version 4.1.0 (R Core Team 2021). For the synthetic control estimates, we used the "synth" package (Abadie et al. 2011).

        In references:
        ```
        Abadie, Alberto, Alexis Diamond, and Jens Hainmueller. 2011. "synth: An R Package for Synthetic Control Methods in Comparative Case Studies." Journal of Statistical Software 42 (13): 1-17.

        R Core Team. 2021. R: A Language and Environment for Statistical Computing. Vienna, Austria: R Foundation for Statistical Computing. https://www.R-project.org/.

        StataCorp. 2021. Stata Statistical Software: Release 17. College Station, TX: StataCorp LLC.
        ```
        """)

st.markdown("<div class='section-header'>Reference and Citation Checklist</div>", unsafe_allow_html=True)

ref_checklist = """
    <ul>
        <li><input type="checkbox"/> All in-text citations follow journal's required format</li>
        <li><input type="checkbox"/> Every in-text citation has a corresponding reference entry</li>
        <li><input type="checkbox"/> All references are in the correct format for the target journal</li>
        <li><input type="checkbox"/> References are in alphabetical order by first author's last name</li>
        <li><input type="checkbox"/> Multiple works by same author are in chronological order</li>
        <li><input type="checkbox"/> All journal names, page ranges, and publication details are complete</li>
        <li><input type="checkbox"/> DOIs or URLs are included when available</li>
        <li><input type="checkbox"/> Data sources are properly cited</li>
        <li><input type="checkbox"/> Software and code citations are included where appropriate</li>
        <li><input type="checkbox"/> Citation style is consistent throughout the paper</li>
    </ul>
    """

st.markdown(ref_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>Proper citation is not just about avoiding plagiarism—it's about positioning your work within the scholarly conversation and giving credit to those whose work has influenced yours. In economics, careful citation practices signal your professionalism and familiarity with the literature in your field.</div>",
	unsafe_allow_html=True)

# Page 12: Submission Process
if selected_page == "1. Title":
    pass

elif selected_page == "2. Abstract":
    pass

# … etc …
elif selected_page == "12. Submission Process":
    st.markdown("<div class='sub-header'>Navigating the Journal Submission Process</div>", unsafe_allow_html=True)

st.markdown("""
    Successfully navigating the submission process requires understanding journal expectations, preparing your 
    manuscript properly, and responding effectively to reviewer feedback. This section guides you through the 
    entire process from journal selection to final publication.
    """)

col1, col2 = create_columns(3, 2)

with col1:
	st.markdown("<div class='section-header'>Selecting Target Journals</div>", unsafe_allow_html=True)
st.markdown("""
        Strategic journal selection is crucial for publication success. Consider these factors:

        1. **Scope and focus**
           - Does the journal publish similar research?
           - Is your topic within their stated scope?
           - Does your methodology align with their typical approach?

        2. **Publication quality metrics**
           - Impact factor and ranking
           - Acceptance rate
           - Time to decision and publication

        3. **Audience and visibility**
           - Who reads this journal?
           - Is it reaching your target audience?
           - How widely is it indexed and available?

        4. **Practical considerations**
           - Page length restrictions
           - Publication fees or charges
           - Open access options
           - Special issue opportunities

        5. **Your career stage and goals**
           - Publication timeline needs
           - Prestige requirements for career advancement
           - Building a coherent research portfolio
        """)

with col2:
	st.markdown("<div class='example'>**Journal Acceptance Rates**</div>", unsafe_allow_html=True)

# Create visualization of acceptance rates
journals = ['American Economic Review', 'Quarterly Journal of Economics',
			'Journal of Political Economy', 'Econometrica',
			'Review of Economic Studies', 'Journal of Economic Literature',
			'American Economic Journal: Applied', 'Journal of Development Economics']

acceptance_rates = [7, 4, 5, 9, 6, 12, 10, 15]  # Approximate acceptance rates in percent

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(journals, acceptance_rates, color='steelblue')

ax.set_xlabel('Acceptance Rate (%)')
ax.set_title('Approximate Acceptance Rates at Top Economics Journals')

for bar in bars:
	width = bar.get_width()
ax.text(width + 0.3, bar.get_y() + bar.get_height() / 2, f'{width}%',
		ha='left', va='center')

plt.tight_layout()
st.pyplot(fig)

st.markdown(
	"<div class='caution'>⚠️ **Caution**: Top-5 economics journals have very low acceptance rates (typically 4-9%). Consider a portfolio strategy with backup journals in case your first choice doesn't accept your paper.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Journal Tiers in Economics</div>", unsafe_allow_html=True)

journal_tiers = pd.DataFrame({
'Tier': [
	'Top-5',
	'General Excellence',
	'Top Field',
	'Solid Field',
	'Regional/Specialized'
],
'Description': [
	'Highest prestige general economics journals',
	'Excellent general journals just below top-5',
	'Leading journals in specific subfields',
	'Respected specialized journals',
	'Focus on specific regions or narrow topics'
],
'Examples': [
	'American Economic Review, Quarterly Journal of Economics, Journal of Political Economy, Econometrica, Review of Economic Studies',
	'Journal of Economic Literature, Journal of Economic Perspectives, Economic Journal, Review of Economics and Statistics, Journal of the European Economic Association',
	'Journal of Finance, Journal of Labor Economics, Journal of Development Economics, Journal of Public Economics, Journal of International Economics',
	'Journal of Urban Economics, Economic Development and Cultural Change, Journal of Environmental Economics and Management',
	'China Economic Review, Eastern Economic Journal, Journal of African Economies'
]
})

st.dataframe(journal_tiers, use_container_width=True)

st.markdown("<div class='section-header'>Preparing Your Manuscript</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Once you've selected a target journal, prepare your manuscript according to their specific guidelines:

        1. **Format requirements**
           - Page length and word count limits
           - Section organization preferences
           - Tables and figures formatting
           - Appendix guidelines

        2. **Style guidelines**
           - Citation and reference formatting
           - Heading and subheading styles
           - Footnote vs. endnote preferences
           - Mathematical notation conventions

        3. **Supplementary materials**
           - Online appendix preparation
           - Data and code availability
           - Additional tables and figures
           - Robustness checks

        4. **Title page and abstract**
           - Required author information
           - Abstract length and structure
           - Keywords selection
           - JEL classification codes
        """)

with col2:
	st.markdown(
		"<div class='tip'>💡 **Tip**: Check the most recently published issues of your target journal to see examples of formatting, structure, and style. Pay particular attention to papers similar to yours in methodology or topic.</div>",
		unsafe_allow_html=True)
st.markdown("<div class='example'>**JEL Classification Codes**</div>", unsafe_allow_html=True)
st.markdown("""
Most economics journals require JEL (Journal of Economic Literature) classification codes. Common codes include:

- **C**: Mathematical and Quantitative Methods
- **D**: Microeconomics
- **E**: Macroeconomics and Monetary Economics
- **F**: International Economics
- **G**: Financial Economics
- **H**: Public Economics
- **I**: Health, Education, and Welfare
- **J**: Labor and Demographic Economics
- **L**: Industrial Organization
- **O**: Economic Development, Innovation, Technological Change
- **Q**: Agricultural and Natural Resource Economics

Choose 1–3 codes that best represent your paper. For the full classification system, visit the AEA website.
""")

st.markdown("<div class='section-header'>Submission Systems and Process</div>", unsafe_allow_html=True)
st.markdown("""
Most economics journals use online submission systems like Editorial Express, Scholar One, or Elsevier Editorial System.
""")

submission_process = pd.DataFrame({
    "Stage": [
        "Initial submission preparation",
        "Author registration",
        "Manuscript upload",
        "Cover letter submission",
        "Suggested reviewers",
        "Editorial screening",
        "Peer review process",
        "Decision letter",
        "Revision or resubmission",
        "Acceptance and publication"
    ],
    "Key Tasks": [
        "Format manuscript according to guidelines, prepare supplementary materials",
        "Create account in journal's submission system, add co-authors and affiliations",
        "Upload manuscript, figures, tables, and appendices in required formats",
        "Craft cover letter addressing editor and explaining paper's contribution",
        "Provide names of potential reviewers (if requested)",
        "Paper reviewed by editors for fit and quality; may be desk rejected",
        "Selected reviewers evaluate manuscript (typically 2–3 months)",
        "Receive decision (reject, revise and resubmit, conditional accept, accept)",
        "Address comments and prepare detailed response letter if revision invited",
        "Final formatting, copyright transfer, proof checking"
    ]
})

st.table(submission_process)

submission_process = pd.DataFrame({
    "Stage": [
        "Initial submission preparation",
        "Author registration",
        "Manuscript upload",
        "Cover letter submission",
        "Suggested reviewers",
        "Editorial screening",
        "Peer review process",
        "Decision letter",
        "Revision or resubmission",
        "Acceptance and publication"
    ],
    "Key Tasks": [
        "Format manuscript according to guidelines, prepare supplementary materials",
        "Create account in journal's submission system, add co-authors and affiliations",
        "Upload manuscript, figures, tables, and appendices in required formats",
        "Craft cover letter addressing editor and explaining paper's contribution",
        "Provide names of potential reviewers (if requested)",
        "Paper reviewed by editors for fit and quality; may be desk rejected",
        "Selected reviewers evaluate manuscript (typically 2–3 months)",
        "Receive decision (reject, revise and resubmit, conditional accept, accept)",
        "Address comments and prepare detailed response letter if revision invited",
        "Final formatting, copyright transfer, proof checking"
    ],
    "Typical Timeline": [
        "1-2 weeks",
        "1 day",
        "1 day",
        "1 day",
        "1 day",
        "1-4 weeks",
        "2-4 months",
        "Brief",
        "1-3 months",
        "2-6 months"
    ]
})

st.dataframe(submission_process, use_container_width=True)



st.markdown("<div class='section-header'>Writing an Effective Cover Letter</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        The cover letter addresses the journal editor and makes the case for why your paper 
        deserves consideration. Key elements include:

        1. **Editor address**: Using the correct editor's name and title

        2. **Paper title and submission statement**: Clearly stating that you're submitting the manuscript

        3. **Research question and significance**: Briefly describing your focus and why it matters

        4. **Key findings and contribution**: Highlighting your main results and contribution to literature

        5. **Fit with journal**: Explaining why the paper is appropriate for this specific journal

        6. **Ethical statements**: Confirming originality, authorship, and lack of concurrent submission

        7. **Special considerations**: Mentioning any special circumstances (e.g., related papers, conflicts)

        8. **Closure**: Thanking the editor for their consideration

        Keep your cover letter concise (typically one page) and focused on why the editor 
        should send your paper for review.
        """)

with col2:
	st.markdown("<div class='example'>**Example Cover Letter**</div>", unsafe_allow_html=True)
st.markdown("""
        Dear Professor [Editor's Name],

        I am pleased to submit the manuscript entitled "[Paper Title]" for consideration for publication in the [Journal Name].

        This paper investigates how changes in banking regulation affect small business lending and entrepreneurship. Using a difference-in-differences approach that exploits staggered implementation of interstate banking deregulation, we find that increased banking competition leads to a 17% increase in small business lending and an 8% increase in new business formation.

        Our paper makes three contributions to the literature. First, we provide causal evidence on the relationship between banking competition and credit access using a novel identification strategy. Second, we demonstrate heterogeneous effects across firm sizes and industries that help explain mixed findings in previous research. Third, we develop a theoretical framework that reconciles our empirical results with existing models of credit market competition.

        We believe this research is well-suited for [Journal Name] given the journal's focus on empirical work at the intersection of finance and economic development, and its recent publications on banking regulation (Smith 2018; Jones 2020).

        This manuscript is not under consideration for publication elsewhere, and all authors have approved the submission. The research was conducted in accordance with ethical standards and did not involve human subjects.

        Thank you for your consideration of our manuscript. We look forward to your response.

        Sincerely,

        [Your Name]
        [Your Affiliation]
        [Contact Information]
        """)

st.markdown("<div class='section-header'>Understanding Journal Decisions</div>", unsafe_allow_html=True)

decision_types = pd.DataFrame({
'Decision': [
	'Desk Reject',
	'Reject After Review',
	'Revise and Resubmit (R&R)',
	'Conditional Accept',
	'Accept'
],
'What It Means': [
	'Paper rejected without external review, typically due to scope or quality issues',
	'Paper sent for review but rejected based on reviewer feedback',
	'Paper has potential but requires substantial changes before reconsideration',
	'Paper will be accepted if specific limited changes are made satisfactorily',
	'Paper accepted for publication (may still require minor edits)'
],
'Typical Frequency': [
	'40-60% of submissions',
	'30-40% of submissions',
	'10-15% of submissions',
	'2-5% of submissions',
	'Very rare for first submissions'
],
'Response Strategy': [
	'Consider feedback for improvement before submitting elsewhere',
	'Carefully evaluate comments, substantially revise, and submit to alternative journal',
	'Address all comments comprehensively with detailed response letter',
	'Make requested changes promptly and thoroughly document them',
	'Complete any final edits and proceed with publication process'
]
})

st.dataframe(decision_types, use_container_width=True)
st.markdown(
    "<div class='caution'>⚠️ **Caution**: In economics, first-round acceptances are extremely rare. The most positive realistic outcome for a first submission to a top journal is a \"revise and resubmit\" decision. Even strong papers typically require at least one round of revisions.</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='section-header'>Timeline Expectations</div>",
    unsafe_allow_html=True
)


# Create visualization of publication timeline
fig, ax = plt.subplots(figsize=(10, 6))

# Timeline stages
stages = ['Initial submission', 'First decision', 'Revision submission',
		  'Second decision', 'Final acceptance', 'Online publication', 'Print publication']

# Cumulative months (approximate)
timelines = [0, 4, 7, 11, 12, 14, 18]

# Plot the timeline
ax.scatter(timelines, stages, s=100, color='steelblue')

# Add connecting lines
for i in range(len(timelines) - 1):
	ax.plot([timelines[i], timelines[i + 1]], [stages[i], stages[i + 1]], 'b-', alpha=0.5)

# Add time spans
for i in range(len(timelines) - 1):
	midpoint = (timelines[i] + timelines[i + 1]) / 2
span = timelines[i + 1] - timelines[i]
ax.text(midpoint, stages[i], f'{span} months', ha='center', va='bottom', color='darkblue')

ax.set_xlabel('Months from Initial Submission')
ax.set_title('Typical Publication Timeline for Top Economics Journals')
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
    The timeline above represents a typical scenario for a paper in a top economics journal. Key points to consider:

    1. **First decision**: Typically takes 3-4 months at top journals
    2. **Revision period**: Authors usually have 2-6 months to revise (varies by journal)
    3. **Subsequent rounds**: Additional revisions may add several more months
    4. **Total time to acceptance**: Often 12-18 months for top journals
    5. **Publication delay**: Additional 3-12 months from acceptance to publication

    Plan your submission strategy accordingly, especially if you have career milestones like job market or tenure reviews.
    """)

st.markdown("<div class='section-header'>Submission Checklist</div>", unsafe_allow_html=True)

submission_checklist = """
    <ul>
        <li><input type="checkbox"/> Manuscript formatted according to journal guidelines</li>
        <li><input type="checkbox"/> Abstract, keywords, and JEL codes prepared</li>
        <li><input type="checkbox"/> Tables and figures properly formatted and numbered</li>
        <li><input type="checkbox"/> References formatted according to journal style</li>
        <li><input type="checkbox"/> Supplementary materials organized (appendices, data, code)</li>
        <li><input type="checkbox"/> Cover letter drafted addressing the appropriate editor</li>
        <li><input type="checkbox"/> All co-authors have approved the submission</li>
        <li><input type="checkbox"/> Contact information for all authors is up-to-date</li>
        <li><input type="checkbox"/> Any potential conflicts of interest disclosed</li>
        <li><input type="checkbox"/> Final proofread for typos and formatting errors</li>
    </ul>
    """

st.markdown(submission_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>The submission process in economics requires patience and persistence. Top journals have high rejection rates, and even eventually successful papers often go through multiple submissions and revisions. View this process as an opportunity to refine and strengthen your work through expert feedback.</div>",
	unsafe_allow_html=True)

# Page 13: Responding to Reviewers
if selected_page == "1. Title":
    pass

elif selected_page == "2. Abstract":
    pass

# … etc …

elif selected_page == "13. Responding to Reviewers":
    st.markdown(
        "<div class='sub-header'>Effectively Responding to Reviewer Comments</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
Receiving a revise and resubmit (R&R) decision is a positive outcome in the competitive world of economics publishing.
How you respond to reviewer comments can make the difference between eventual acceptance and rejection. This section
provides strategies for addressing reviewer feedback effectively.
"""
    )

col1, col2 = create_columns(3, 2)

with col1:
	st.markdown("<div class='section-header'>Understanding Reviewer Feedback</div>", unsafe_allow_html=True)
st.markdown("""
        Reviewer comments in economics typically fall into several categories:

        1. **Substantive issues**
           - Theoretical framework concerns
           - Methodological critiques
           - Identification strategy challenges
           - Interpretation questions

        2. **Major revisions**
           - Additional analyses or robustness checks
           - Restructuring of arguments
           - Reframing of contributions
           - New literature connections

        3. **Minor revisions**
           - Clarification requests
           - Additional references
           - Editing suggestions
           - Presentation improvements

        4. **Technical issues**
           - Statistical procedures
           - Econometric specifications
           - Mathematical derivations
           - Computational methods

        Understanding which category each comment falls into helps prioritize your response strategy.
        """)

with col2:
	st.markdown("<div class='example'>**Interpreting Decision Letters**</div>", unsafe_allow_html=True)

# Create decision letter terminology table
letter_terms = pd.DataFrame({
'Phrase': [
	'"Potential contribution"',
	'"Interesting but preliminary"',
	'"Major concerns"',
	'"Substantial revision required"',
	'"If adequately addressed"',
	'"Not enthusiastic"',
	'"Not guaranteed"'
],
'What It Usually Means': [
	'Editor sees value but needs convincing',
	'Significant additional work needed',
	'Fundamental issues that must be resolved',
	'Paper requires extensive changes',
	'Editor is open to acceptance if you satisfy reviewers',
	'Chances of acceptance are lower',
	'Even with changes, acceptance isnt assured'
]
})

st.dataframe(letter_terms, use_container_width=True)

st.markdown(
	"<div class='tip'>💡 **Tip**: Pay careful attention to the editor's letter, which often provides guidance on which reviewer comments are most important to address. The editor makes the final decision, so their priorities should influence your revision strategy.</div>",
	unsafe_allow_html=True)

st.markdown("<div class='section-header'>Preparing Your Response</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Before diving into revisions, develop a strategic approach:

        1. **Initial assessment**
           - Read all comments carefully without responding immediately
           - Categorize comments by importance and difficulty
           - Identify any contradictory suggestions between reviewers
           - Note the editor's specific guidance

        2. **Revision planning**
           - Create a point-by-point response outline
           - Determine which comments require new analyses
           - Identify comments that may require pushback
           - Estimate time needed for each major revision

        3. **Strategic decisions**
           - Which suggestions improve the paper?
           - Where might you respectfully disagree?
           - Are any requested analyses infeasible?
           - How will you handle contradictory comments?

        4. **Timeline and resources**
           - Plan realistic timeline for revisions
           - Identify needed resources (data, computing, assistance)
           - Consider requesting deadline extension if necessary
        """)

with col2:
	st.markdown("<div class='example'>**Comment Classification Framework**</div>", unsafe_allow_html=True)

# Create comment classification matrix
fig, ax = plt.subplots(figsize=(8, 8))

# Create a 2x2 matrix
ax.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0], 'k-', linewidth=2)
ax.plot([5, 5], [0, 10], 'k-', linewidth=1.5)
ax.plot([0, 10], [5, 5], 'k-', linewidth=1.5)

# Add text labels
ax.text(2.5, 7.5, 'Critical\nHigh Effort', ha='center', va='center', fontsize=12)
ax.text(7.5, 7.5, 'Critical\nLow Effort', ha='center', va='center', fontsize=12)
ax.text(2.5, 2.5, 'Non-Critical\nHigh Effort', ha='center', va='center', fontsize=12)
ax.text(7.5, 2.5, 'Non-Critical\nLow Effort', ha='center', va='center', fontsize=12)

# Add axis labels
ax.text(5, -0.5, 'Effort Required', ha='center', va='center', fontsize=14)
ax.text(-0.5, 5, 'Importance', ha='center', va='center', rotation=90, fontsize=14)

# Add examples in each quadrant
ax.text(2.5, 6.5, 'Example: Identification\nstrategy concerns', ha='center', va='center', fontsize=10, color='darkblue')
ax.text(7.5, 6.5, 'Example: Missing key\nreferences', ha='center', va='center', fontsize=10, color='darkblue')
ax.text(2.5, 3.5, 'Example: Additional\nrobustness checks', ha='center', va='center', fontsize=10, color='darkblue')
ax.text(7.5, 3.5, 'Example: Clarification of\nterminology', ha='center', va='center', fontsize=10, color='darkblue')

# Remove ticks and axes
ax.set_xticks([])
ax.set_yticks([])

ax.set_title('Comment Classification Framework')
plt.tight_layout()
st.pyplot(fig)

st.markdown("<div class='section-header'>Response Letter Structure</div>", unsafe_allow_html=True)

st.markdown("""
    A well-structured response letter is crucial for demonstrating how thoroughly you've addressed reviewer concerns.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Your response letter should include:

        1. **Introductory section**
           - Thank editor and reviewers
           - Summarize major changes
           - Overview of revision approach
           - Response to editor's specific concerns

        2. **Point-by-point responses**
           - Quote each reviewer comment verbatim
           - Respond to each point individually
           - Explain changes made in the manuscript
           - Provide page/section references to changes

        3. **Additional changes section**
           - Note any other improvements
           - Explain updates to data or methods
           - Mention new literature incorporated

        4. **Closing**
           - Express appreciation for the process
           - Note how the paper has improved
           - Affirm willingness to make further changes
        """)

with col2:
	st.markdown(
		"<div class='example'>**Example Response Letter Introduction**</div>",
		unsafe_allow_html=True
	)
	st.markdown("""
	Dear Professor [Editor's Name],

	Thank you for the opportunity to revise our manuscript "[Paper Title]" (MS #123456) for [Journal Name]. We appreciate the constructive feedback from you and the reviewers, which has helped us significantly improve the paper.

	In this revision, we have addressed all the comments and suggestions. The major changes include:

	1. Strengthening our identification strategy by incorporating an instrumental variable approach (Reviewer 1, Major Comment 1)  
	2. Expanding the theoretical framework to better connect with the empirical analysis (Reviewer 2, Major Comment 1)  
	3. Adding robustness checks using alternative measures and specifications (Reviewers 1 and 2)  
	4. Clarifying our contribution relative to the existing literature, particularly Smith (2019) and Jones (2020) (Editor and Reviewer 1)  
	5. Improving the presentation of results with additional figures and tables (Reviewer 2)  

	Below, we provide detailed responses to each comment. Changes in the manuscript are highlighted in blue text for easy identification.
	""")

	st.markdown(
		"<div class='section-header'>Responding to Different Types of Comments</div>",
		unsafe_allow_html=True
	)

	response_strategies = pd.DataFrame({
		"Comment Type": [
			"Identification concerns",
			"Theoretical framework",
			"Robustness requests",
			"Literature additions",
			"Interpretation questions",
			"Presentation issues",
			"Contradictory suggestions",
			"Infeasible requests"
		],
		"Response Strategy": [
			"Address head-on with additional tests or improved approach",
			"Strengthen theoretical grounding and connections to empirics",
			"Conduct reasonable additional tests, explain results clearly",
			"Add relevant references with substantive discussion",
			"Clarify reasoning and provide additional context",
			"Improve tables/figures and explanations",
			"Acknowledge both viewpoints, choose path with explanation",
			"Explain constraints honestly, offer alternatives"
		],
		"Example Response": [
			"We have strengthened our identification strategy by implementing an instrumental variable approach using X as an instrument for Y. See new Section 4.2 and Table 5.",
			"We have expanded our theoretical framework in Section 2 to explicitly connect comparative statics predictions with our empirical specifications. New equation (4) maps to our main estimating equation.",
			"We have conducted the suggested robustness checks using alternative measures of X. Results remain qualitatively similar (new Appendix Table A3).",
			"We have incorporated the suggested literature on X, particularly Smith (2019) and Jones (2020), in Section 2.3 and discussed methodological differences.",
			"We have clarified our interpretation of the results in Section 5.1, linking findings to theoretical mechanisms and addressing alternative explanations.",
			"We have redesigned Figure 3 to clearly show treatment effects over time with confidence intervals and distinct group markers.",
			"Reviewers 1 and 2 offered contrasting control-variable suggestions. We followed Reviewer 1’s recommendation (with explanation) and included Reviewer 2’s specification in robustness checks.",
			"The suggested individual-level analysis is not feasible due to data access constraints. Instead, we conducted an alternative group-level analysis (new Table 6)."
		]
	})
	st.table(response_strategies)

st.dataframe(response_strategies, use_container_width=True)

st.markdown("<div class='section-header'>Handling Difficult Comments</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Some reviewer comments present special challenges. Here are strategies for handling difficult situations:

        1. **When you disagree with a reviewer**
           - Acknowledge the concern respectfully
           - Provide clear evidence or reasoning for your position
           - Consider adding analysis that addresses the underlying issue
           - Offer compromise where possible

        2. **When comments are contradictory**
           - Note the contradiction explicitly
           - Explain your chosen approach
           - Consider accommodating both perspectives if possible
           - Defer to editor's guidance if provided

        3. **When comments request infeasible analysis**
           - Explain constraints honestly (data limitations, etc.)
           - Offer alternative approaches that address the concern
           - Provide partial analysis if possible
           - Consider adding discussion of limitations

        4. **When comments miss your point**
           - Recognize that unclear writing likely contributed
          6 - Clarify your argument or finding
           - Improve related sections for clarity
           - Avoid suggesting the reviewer misunderstood
        """)

with col2:
	st.markdown("<div class='example'>**Example Response to a Disagreement**</div>", unsafe_allow_html=True)
st.markdown("""
        **Reviewer comment**: "The authors use OLS for their main specification, but this approach cannot address the obvious endogeneity problem. The results are therefore biased and uninformative."

        **Effective response**:

        > We appreciate the reviewer's concern about potential endogeneity in our estimation. While we agree that endogeneity is a theoretical concern, we respectfully believe that the specific institutional context of our study substantially mitigates this issue for three reasons:

        > First, the policy change we study was implemented based on predetermined characteristics that are not correlated with our outcome variables, as we show in new Table 4, which tests for correlations between implementation timing and pre-trend outcomes.

        > Second, our difference-in-differences approach with entity and time fixed effects addresses time-invariant confounders and common temporal shocks.

        > Third, we now include an instrumental variable approach as a robustness check (new Section 4.3 and Table 7), using the geographic distance to the nearest implementing region as an instrument. The IV results are consistent with our main findings, though less precisely estimated.

        > We have clarified these points in the paper (pages 12-14) and added a more thorough discussion of identification assumptions.
        """)

st.markdown(
    "<div class='caution'>⚠️ **Caution**: Avoid defensive or dismissive language when disagreeing with reviewers. Phrases like \"the reviewer misunderstood\", \"the reviewer is wrong\", or \"this comment is irrelevant\" can create a negative impression. Instead, focus on substantive responses that address the underlying concerns.</div>",
    unsafe_allow_html=True
)


st.markdown("<div class='section-header'>Tracking and Highlighting Changes</div>", unsafe_allow_html=True)

st.markdown("""
    Make it easy for editors and reviewers to see how you've addressed their comments:
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        1. **Visual highlighting**
           - Use colored text for new or modified content
           - Consider a marked-up version and a clean version
           - Use margin comments for complex changes

        2. **Page and section references**
           - Provide specific page numbers for each change
           - Reference section numbers and figure/table numbers
           - Use precise quotes for small text changes

        3. **Change summary document**
           - Provide a concise overview of major changes
           - Group related changes by section or theme
           - Note additions, deletions, and reorganizations

        4. **Response-to-changes mapping**
           - Create clear links between responses and changes
           - Use consistent numbering or coding system
           - Ensure every comment has an identifiable response
        """)

with col2:
	st.markdown(
		"<div class='tip'>💡 **Tip**: Create a revision tracking spreadsheet with columns for: (1) Reviewer comment, (2) Response plan, (3) Changes implemented, (4) Location in revised manuscript, and (5) Status. This helps manage complex revisions with multiple reviewer requests.</div>",
		unsafe_allow_html=True)

st.markdown("<div class='example'>**Example Point-by-Point Response**</div>", unsafe_allow_html=True)
st.markdown("""
        **Reviewer 1, Comment 3**: "The authors claim their results are robust, but they do not examine how their findings might change with alternative measures of the key dependent variable."

        **Response**: We thank the reviewer for this excellent suggestion. We have conducted additional robustness checks using three alternative measures of our dependent variable:

        1. A continuous measure instead of the binary indicator (new Table 5, column 1)
        2. A log-transformed version to address skewness (Table 5, column 2)
        3. An alternative definition based on Smith (2018) (Table 5, column 3)

        These results confirm our main findings, with effect sizes ranging from 0.14 to 0.19, all statistically significant at the 5% level. We have added discussion of these robustness checks in Section 5.2 (pages 18-19).
        """)

st.markdown("<div class='section-header'>Revise and Resubmit Success Rates</div>", unsafe_allow_html=True)

# Create visualization of R&R success rates
journals = ['AER', 'QJE', 'JPE', 'Econometrica', 'REStud', 'AEJ: Applied', 'JDE', 'JHR']
success_rates = [60, 55, 58, 50, 52, 65, 70, 68]  # approximate R&R success rates in percent

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(journals, success_rates, color='steelblue')

ax.set_ylabel('R&R Success Rate (%)')
ax.set_title('Approximate Success Rates for Revise & Resubmit Papers')

for bar in bars:
	height = bar.get_height()
ax.text(bar.get_x() + bar.get_width() / 2., height + 1, f'{height}%',
		ha='center', va='bottom')

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
    While first-round acceptance rates in top economics journals are very low (often <1%), papers that receive an R&R have 
    much better chances, typically 50-70%. This underscores the importance of responding effectively to reviewer comments.

    Factors that influence R&R success:

    1. **Comprehensiveness of response**: Addressing all comments thoroughly
    2. **Quality of revisions**: Making substantive improvements, not just superficial changes
    3. **Response letter quality**: Clear, point-by-point responses with specific references
    4. **Time taken**: Using sufficient time to implement meaningful changes
    5. **Clarity of changes**: Making it easy for reviewers to see what you've done
    """)

st.markdown("<div class='section-header'>Reviewer Response Checklist</div>", unsafe_allow_html=True)

response_checklist = """
    <ul>
        <li><input type="checkbox"/> Created point-by-point response addressing every comment</li>
        <li><input type="checkbox"/> Implemented all feasible requested changes</li>
        <li><input type="checkbox"/> Provided clear justification for any disagreements</li>
        <li><input type="checkbox"/> Referenced specific page numbers and sections for changes</li>
        <li><input type="checkbox"/> Highlighted or marked changes in the manuscript</li>
        <li><input type="checkbox"/> Addressed editor's comments with particular attention</li>
        <li><input type="checkbox"/> Used respectful, professional tone throughout</li>
        <li><input type="checkbox"/> Explained how changes improve the paper</li>
        <li><input type="checkbox"/> Checked that response letter is well-organized and comprehensive</li>
        <li><input type="checkbox"/> Verified that all attachments and supplementary materials are included</li>
    </ul>
    """

st.markdown(response_checklist, unsafe_allow_html=True)

st.markdown(
	"<div class='highlight'>The revision process is an opportunity to significantly strengthen your paper. Even when you disagree with specific comments, consider the underlying concerns that motivated them. Reviewers and editors want to help you produce the best possible version of your work, and taking their feedback seriously demonstrates your commitment to scholarly rigor.</div>",
	unsafe_allow_html=True)

# Page 14: Resources & Templates
if selected_page == "1. Title":
    pass

elif selected_page == "2. Abstract":
    pass

# … other pages …

elif selected_page == "14. Resources & Templates":
    st.markdown(
        "<div class='sub-header'>Resources and Templates for Economics Papers</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
This section provides practical resources, templates, and tools to help you streamline your research 
and writing process for economics papers. These resources can save time and improve the quality of your submissions.
"""
    )

    st.markdown(
        "<div class='section-header'>LaTeX Templates for Economics Papers</div>",
        unsafe_allow_html=True
    )


st.markdown("<div class='section-header'>LaTeX Templates for Economics Papers</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        LaTeX is the preferred format for most economics papers, especially those with mathematical content. 
        Here are recommended templates:

        1. **AEA LaTeX Template**
           - Official template for American Economic Review and other AEA journals
           - Includes proper formatting, bibliography style, and table/figure handling
           - Available on the AEA website

        2. **Econometrica Template**
           - Specific formatting for Econometrica submissions
           - Specialized bibliography style
           - Available on the journal website

        3. **Generic Economics Template**
           - Adaptable for multiple journals
           - Clean formatting with standard economics features
           - Available on templates sites like Overleaf

        4. **Job Market Paper Template**
           - Designed for PhD candidates' job market papers
           - Professional formatting with clear structure
           - Available through economics department resources
        """)

with col2:
	st.markdown(
		"<div class='tip'>💡 **Tip**: Overleaf (overleaf.com) offers online LaTeX editing with many economics templates pre-loaded. It simplifies collaboration and version control while handling LaTeX compilation automatically.</div>",
		unsafe_allow_html=True)

st.markdown("<div class='example'>**Key LaTeX Packages for Economics Papers**</div>", unsafe_allow_html=True)

# Create table of useful LaTeX packages
latex_packages = pd.DataFrame({
	'Package': [
'natbib',
'booktabs',
'dcolumn',
'graphicx',
'threeparttable',
'amsmath',
'hyperref',
'tikz',
'estout',
'setspace'
],
'Purpose': [
'Advanced citation and bibliography handling',
'Professional table formatting',
'Decimal-aligned columns in tables',
'Figure inclusion and manipulation',
'Tables with notes and sources',
'Mathematical equations and environments',
'Hyperlinks and PDF bookmarks',
'Creating diagrams and custom figures',
'Converting Stata output to LaTeX tables',
'Line spacing control'
]
})

st.dataframe(latex_packages, use_container_width=True)

st.markdown("<div class='section-header'>Research Organization Tools</div>", unsafe_allow_html=True)

research_tools = pd.DataFrame({
	'Category': [
'Project Management',
'Reference Management',
'Data Analysis',
'Writing Environment',
'Figure Creation',
'Table Generation',
'Version Control',
'Collaborative Editing',
'Paper Organization',
'Preregistration'
],
'Recommended Tools': [
'Trello, Asana, Notion',
'Zotero, Mendeley, EndNote, JabRef',
'Stata, R, Python, MATLAB',
'Overleaf, RStudio, VS Code with LaTeX extensions',
'R with ggplot2, Python with matplotlib, Stata graphs',
'estout (Stata), stargazer (R), regression tables (Python)',
'Git, GitHub, Bitbucket',
'Overleaf, Google Docs, Microsoft Office 365',
'Scrivener, Notion, LyX',
'OSF, AEA RCT Registry, AsPredicted'
],
'Economics-Specific Features': [
'Research workflow templates for empirical projects',
'Economics citation styles, econ paper organization',
'Econometrics packages, standard error adjustments',
'Economics journal templates, equation handling',
'Publication-quality regression plots, coefficient plots',
'Regression tables with standard errors and significance stars',
'Tracking changes to code, data, and manuscripts',
'Equation editing, mathematical notation sharing',
'IMRAD structure templates, section management',
'Pre-analysis plans for field experiments'
]
})

st.dataframe(research_tools, use_container_width=True)

st.markdown("<div class='section-header'>Creating Publication-Quality Tables</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Table formatting is crucial for economics papers. Well-designed tables present your results clearly and professionally.

        **Key principles**:

        1. **Clear structure**
           - Logical organization of variables
           - Consistent column formatting
           - Appropriate grouping of related variables

        2. **Statistical reporting**
           - Coefficients with standard errors
           - Significance stars or p-values
           - Effect sizes and confidence intervals

        3. **Model information**
           - Sample size
           - R-squared or relevant fit statistics
           - Fixed effects notation
           - Clustering information

        4. **Comprehensive notes**
           - Variable definitions
           - Data sources
           - Estimation method
           - Significance level indicators
        """)

with col2:
	st.markdown("<div class='example'>**Stata to LaTeX Table Example**</div>", unsafe_allow_html=True)
st.markdown("""
        ```stata
        * Stata code for publication-quality tables
        ssc install estout  // Install if needed

        // Run regressions and store results
        eststo clear
        eststo: reg y x1 x2
        eststo: reg y x1 x2 x3
        eststo: reg y x1 x2 x3 x4

        // Generate LaTeX table
        esttab using "results_table.tex", ///
            label replace booktabs ///
            b(3) se(3) star(* 0.10 ** 0.05 *** 0.01) ///
            scalars("N Observations" "r2 R-squared") ///
            mtitles("Model 1" "Model 2" "Model 3") ///
            addnotes("Standard errors in parentheses." ///
                     "* p<0.10, ** p<0.05, *** p<0.01")
        ```

        **R code example**:
        ```r
        # R code for publication-quality tables
        library(stargazer)

        # Run regressions
        model1 <- lm(y ~ x1 + x2, data=df)
        model2 <- lm(y ~ x1 + x2 + x3, data=df)
        model3 <- lm(y ~ x1 + x2 + x3 + x4, data=df)

        # Generate LaTeX table
        stargazer(model1, model2, model3,
                  title="Regression Results",
                  column.labels=c("Model 1", "Model 2", "Model 3"),
                  align=TRUE,
                  covariate.labels=c("Variable 1", "Variable 2", 
                                    "Variable 3", "Variable 4"),
                  model.numbers=FALSE,
                  type="latex",
                  out="results_table.tex")
        ```
        """)

st.markdown("<div class='section-header'>Creating Publication-Quality Figures</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        Effective figures can dramatically improve the impact of your economics paper.

        **Key principles**:

        1. **Clarity and simplicity**
           - Clean, uncluttered design
           - Clear labels and legends
           - Appropriate scale and proportions

        2. **Information density**
           - Show the data, not just summary statistics
           - Include confidence intervals where appropriate
           - Consider multiple related panels in one figure

        3. **Visual accessibility**
           - Color choices that work in grayscale
           - Patterns that remain distinguishable when printed
           - Sufficient font size for labels

        4. **Technical requirements**
           - Vector formats (PDF, EPS) for line drawings
           - High-resolution (300+ dpi) for raster images
           - Consistent style across all figures
        """)

with col2:
	st.markdown("<div class='example'>**R ggplot2 Figure Example**</div>", unsafe_allow_html=True)
st.markdown("""
        ```r
        # R code for publication-quality figures
        library(ggplot2)
        library(dplyr)

        # Create event study plot
        event_study_plot <- ggplot(event_data, 
            aes(x=period, y=estimate, ymin=lower, ymax=upper)) +
            geom_point() +
            geom_errorbar(width=0.2) +
            geom_hline(yintercept=0, linetype="dashed") +
            geom_vline(xintercept=0, linetype="dashed") +
            theme_bw() +
            labs(
                x = "Quarters Relative to Policy Change",
                y = "Treatment Effect",
                title = "Event Study: Policy Impact on Outcome"
            ) +
            theme(
                legend.position = "bottom",
                panel.grid.minor = element_blank(),
                text = element_text(size = 12),
                plot.title = element_text(size = 14, hjust = 0.5)
            )

        # Save as PDF for publication
        ggsave("event_study.pdf", event_study_plot, 
               width = 7, height = 5, units = "in")
        ```

        **Stata code example**:
        ```stata
        * Stata code for coefficient plot
        ssc install coefplot  // Install if needed

        // Run regressions and store
        reg y x1 x2 x3 x4, robust
        estimates store m1
        reg y x1 x2 x3 x4 i.fe, cluster(id)
        estimates store m2

        // Create coefficient plot
        coefplot m1 m2, keep(x1 x2 x3 x4) ///
            xline(0) grid(none) ///
            coeflabels(x1="Variable 1" x2="Variable 2" ///
                      x3="Variable 3" x4="Variable 4") ///
            legend(order(1 "Baseline" 2 "With Fixed Effects")) ///
            title("Coefficient Estimates") ///
            xtitle("Effect Size") ///
            graphregion(color(white)) bgcolor(white)

        // Export as EPS for publication
        graph export "coef_plot.eps", replace
        ```
        """)

st.markdown("<div class='section-header'>Data and Code Management</div>", unsafe_allow_html=True)

st.markdown("""
    Good data and code management practices are essential for reproducible research and are increasingly required 
    by economics journals.
    """)

col1, col2 = create_columns()

with col1:
	st.markdown("""
        **Best practices for data management**:

        1. **Raw data preservation**
           - Store original unmodified data
           - Document source and access date
           - Include data citations

        2. **Processing transparency**
           - Separate data cleaning scripts
           - Document all transformations
           - Create analysis-ready datasets

        3. **Variable documentation**
           - Clear variable names
           - Comprehensive codebooks
           - Units of measurement

        4. **Directory structure**
           - Organized folder hierarchy
           - Consistent naming conventions
           - README files explaining contents

        5. **Version control**
           - Track changes to datasets
           - Record dataset versions used in analyses
           - Document data updates
        """)

with col2:
	st.markdown("""
        **Best practices for code management**:

        1. **Code organization**
           - Modular scripts with specific purposes
           - Clear naming conventions
           - Logical workflow sequence

        2. **Documentation**
           - Header comments explaining purpose
           - In-line comments for complex operations
           - Function documentation

        3. **Reproducibility**
           - Set random seeds for stochastic processes
           - Record software versions
           - Manage package dependencies

        4. **Version control**
           - Use Git or similar version control
           - Commit frequently with descriptive messages
           - Tag versions used for specific analyses

        5. **Master scripts**
           - Create master do-files or scripts
           - Enable one-click reproduction
           - Document expected runtime
        """)

st.markdown("<div class='example'>**Example Project Directory Structure**</div>", unsafe_allow_html=True)
st.markdown("""
    ```
    project/
    ├── README.md                 # Project overview and instructions
    ├── data/
    │   ├── raw/                  # Original unmodified data
    │   ├── processed/            # Cleaned and processed data
    │   └── final/                # Analysis-ready datasets
    ├── code/
    │   ├── 01_data_cleaning.do   # Data preparation scripts
    │   ├── 02_analysis.do        # Main analysis scripts
    │   ├── 03_robustness.do      # Robustness checks
    │   └── 04_figures_tables.do  # Output generation
    ├── output/
    │   ├── figures/              # Generated figures
    │   ├── tables/               # Generated tables
    │   └── appendix/             # Supplementary results
    ├── paper/
    │   ├── main.tex              # Main manuscript
    │   ├── appendix.tex          # Online appendix
    │   └── bibliography.bib      # References
    └── admin/                    # Administrative documents
        ├── submission_checklist.md
        ├── journal_requirements.md
        └── response_to_reviewers.md
    ```
    """)

st.markdown("<div class='section-header'>Econometric Code Templates</div>", unsafe_allow_html=True)

with st.expander("Difference-in-Differences Template"):
	st.markdown("""
        **Stata Code**:
        ```stata
        * Basic DiD estimation
        reg y i.treated i.post i.treated#i.post x1 x2 x3, cluster(id)

        * DiD with fixed effects
        reghdfe y i.treated#i.post x1 x2 x3, absorb(id period) cluster(id)

        * Event study specification
        reghdfe y i.treated#i.period x1 x2 x3, absorb(id period) cluster(id)

        * Plotting event study coefficients
        coefplot, keep(*.treated#*.period) vertical yline(0) xlabel(, angle(vertical))

        * Testing parallel trends
        reg y i.treated#i.pre_period x1 x2 x3 if post==0, cluster(id)
        test 1.treated#2.pre_period 1.treated#3.pre_period 1.treated#4.pre_period
        ```

        **R Code**:
        ```r
        # Basic DiD
        did_model <- lm(y ~ treated * post + x1 + x2 + x3, data = df)
        summary(did_model)

        # DiD with fixed effects
        library(fixest)
        did_fe <- feols(y ~ treated:post + x1 + x2 + x3 | id + period, 
                      data = df, cluster = "id")
        summary(did_fe)

        # Event study
        event_study <- feols(y ~ i(period, treated, ref = -1) + x1 + x2 + x3 | 
                           id + period, 
                         data = df, cluster = "id")

        # Plot event study
        library(ggplot2)
        iplot(event_study, main = "Event Study", xlab = "Period")
        ```
        """)

with st.expander("Instrumental Variables Template"):
	st.markdown("""
        **Stata Code**:
        ```stata
        * First-stage regression
        reg endogenous_var instrument x1 x2 x3, robust
        est store first_stage

        * Test for weak instruments
        estat firststage

        * 2SLS estimation
        ivregress 2sls y (endogenous_var = instrument) x1 x2 x3, robust
        est store iv_model

        * OLS for comparison
        reg y endogenous_var x1 x2 x3, robust
        est store ols_model

        * Display results
        esttab first_stage iv_model ols_model, se star(* 0.10 ** 0.05 *** 0.01) ///
               stats(N r2 F) mtitles("First Stage" "IV" "OLS")
        ```

        **R Code**:
        ```r
        library(AER)
        library(lmtest)
        library(sandwich)

        # First stage
        first_stage <- lm(endogenous_var ~ instrument + x1 + x2 + x3, data = df)
        summary(first_stage)

        # F-statistic for instrument strength
        linearHypothesis(first_stage, "instrument = 0")

        # 2SLS
        iv_model <- ivreg(y ~ endogenous_var + x1 + x2 + x3 | 
                        instrument + x1 + x2 + x3, 
                       data = df)

        # Robust standard errors
        coeftest(iv_model, vcov = vcovHC(iv_model, type = "HC1"))

        # OLS for comparison
        ols_model <- lm(y ~ endogenous_var + x1 + x2 + x3, data = df)
        ```
        """)

with st.expander("Regression Discontinuity Design Template"):
	st.markdown("""
        **Stata Code**:
        ```stata
        * Install required packages
        ssc install rdrobust
        ssc install rddensity

        * Density test for manipulation
        rddensity running_var, c(0)

        * RD estimation
        rdrobust y running_var, c(0)

        * RD with covariates
        rdrobust y running_var, c(0) covs(x1 x2 x3)

        * Bandwidth sensitivity
        rdrobust y running_var, c(0) h(5 10 15)

        * Plotting RD
        rdplot y running_var, c(0) graph_options(title("RD Plot") xtitle("Running Variable") ytitle("Outcome"))
        ```

        **R Code**:
        ```r
        library(rdrobust)
        library(rddensity)

        # Density test for manipulation
        manip_test <- rddensity(df$running_var, c = 0)
        summary(manip_test)

        # Basic RD estimation
        rd_est <- rdrobust(df$y, df$running_var, c = 0)
        summary(rd_est)

        # RD with covariates
        rd_cov <- rdrobust(df$y, df$running_var, c = 0, 
                         covs = cbind(df$x1, df$x2, df$x3))
        summary(rd_cov)

        # Bandwidth sensitivity
        rd_bw <- rdrobust(df$y, df$running_var, c = 0, h = c(5, 10, 15))
        summary(rd_bw)

        # RD plot
        rd_plot <- rdplot(df$y, df$running_var, c = 0, 
                       title = "RD Plot", 
                       x.label = "Running Variable", 
                       y.label = "Outcome")
        ```
        """)

st.markdown("<div class='section-header'>Standard Templates for Common Paper Elements</div>", unsafe_allow_html=True)

with st.expander("Abstract Template"):
	st.markdown("""
        ```
        This paper examines [research question] using [data/methodology approach]. 
        [Brief context or motivation]. 
        We find that [key finding 1] and [key finding 2]. 
        These results [support/challenge] the view that [theoretical implication] and 
        contribute to the literature by [specific contribution]. 
        Our findings have implications for [policy area or economic understanding].
        ```

        **Example**:

        > This paper examines how financial deregulation affects small business lending and entrepreneurship using branch-level banking data from 1994-2007. While prior research has documented a correlation between financial development and economic growth, causal evidence has been limited. We find that interstate banking deregulation increased small business lending by 17% and new business formation by 8% in affected markets. These results support the view that credit constraints significantly impact entrepreneurial activity and contribute to the literature by establishing a causal link between banking competition and business dynamism. Our findings have implications for current debates on financial regulation, suggesting that policies promoting competition in local banking markets may stimulate entrepreneurship and economic growth.
        """)

with st.expander("Data Sources and Summary Statistics Section Template"):
	st.markdown("""
        ```
        3. Data Sources and Summary Statistics

        3.1 Data Sources

        This paper uses data from [primary data source] covering [time period] for [population/sample]. 
        The data includes [key variables or measures] and was collected by [organization] using [collection method].
        [Additional details about sample construction or selection].

        We supplement this primary data with [secondary data sources] to obtain [additional variables].
        [Any details about data merging or linkage].

        3.2 Sample Construction

        Our analysis sample consists of [units of observation] that meet the following criteria:
        [List inclusion/exclusion criteria].
        The final sample contains [sample size] observations representing [coverage percentage] of the [relevant population].

        3.3 Variable Construction

        Our primary outcome variable, [outcome], is measured as [precise definition].
        The key independent variable, [independent variable], is defined as [precise definition].
        Control variables include [list of controls] which account for [potential confounders].

        3.4 Summary Statistics

        Table 1 presents summary statistics for our main analysis sample. The average [outcome variable] is [mean value] 
        with a standard deviation of [SD value]. The mean value of [key independent variable] is [mean value].
        [Note any important patterns or differences across groups if relevant].

        [Reference to Table 1 here]
        ```

        **Table 1 would typically follow this format**:

        | Variable | Mean | Std. Dev. | Min | Max | N |
        |----------|------|-----------|-----|-----|---|
        | Outcome Variable | 0.XX | 0.XX | 0.XX | 0.XX | XXX |
        | Key Independent Var | 0.XX | 0.XX | 0.XX | 0.XX | XXX |
        | Control 1 | 0.XX | 0.XX | 0.XX | 0.XX | XXX |
        | Control 2 | 0.XX | 0.XX | 0.XX | 0.XX | XXX |
        | ... | ... | ... | ... | ... | ... |

        Notes: This table presents summary statistics for the main analysis sample. The sample includes [sample description]. All monetary values are in [currency and year].
        """)

with st.expander("Empirical Strategy Section Template"):
	st.markdown("""
        ```
        4. Empirical Strategy

        4.1 Baseline Specification

        To estimate the effect of [independent variable] on [outcome], we employ the following specification:

        Y_{it} = β₀ + β₁X_{it} + γZ_{it} + α_i + δ_t + ε_{it}     (1)

        where Y_{it} is [outcome] for [unit] i in time t, X_{it} is [independent variable], Z_{it} is a vector of control variables including [list key controls], α_i represents [unit] fixed effects, δ_t represents time fixed effects, and ε_{it} is the error term. The coefficient of interest is β₁, which represents [interpretation of coefficient].

        Standard errors are clustered at the [level] level to account for [type of correlation in error terms].

        4.2 Identification Strategy

        The main identification challenge is [describe endogeneity concern]. To address this concern, we employ [identification approach] which relies on [source of variation]. This approach is valid under the assumption that [key identifying assumption].

        To assess this assumption, we conduct several tests. First, we [first validation approach]. Second, we [second validation approach]. These tests, presented in Section 5.3, support the validity of our identification strategy.

        4.3 Alternative Specifications

        We consider several alternative specifications to assess the robustness of our results. First, we [first robustness approach]. Second, we [second robustness approach]. Third, we [third robustness approach]. These specifications help address concerns about [potential threats to identification].
        ```
        """)

with st.expander("Response to Reviewers Template"):
	st.markdown("""
        ```
        Response to Reviewers

        Manuscript: [Title]
        Manuscript Number: [Number]

        Dear [Editor Name],

        We thank you for the opportunity to revise our manuscript. We appreciate the constructive feedback from you and the reviewers, which has helped us significantly improve the paper. We have addressed all comments and suggestions as detailed below.

        In response to your editorial guidance, we have particularly focused on [main editorial concerns].

        Below, we provide point-by-point responses to each reviewer's comments. The changes in the manuscript are highlighted in blue text for easy identification.

        Reviewer #1:

        Comment 1: "[Verbatim comment]"

        Response: We thank the reviewer for this helpful suggestion. We have [action taken] as suggested. Specifically, we [details of changes]. This change appears on page XX of the revised manuscript.

        Comment 2: "[Verbatim comment]"

        Response: We appreciate this important point. We have addressed it by [action taken]. The new analysis shows [brief result]. We have added this discussion on pages XX-XX.

        [Continue with all comments from Reviewer #1]

        Reviewer #2:

        [Same format for Reviewer #2's comments]

        Additional Changes:

        Beyond the reviewers' suggestions, we have made the following improvements to the manuscript:

        1. [Additional change 1]
        2. [Additional change 2]

        We believe these revisions have substantially strengthened the paper, and we hope that the manuscript is now suitable for publication in [Journal Name]. We remain open to any additional suggestions for improvement.

        Sincerely,

        [Authors]
        ```
        """)

st.markdown("<div class='section-header'>Final Resources and Links</div>", unsafe_allow_html=True)

col1, col2 = create_columns()

with col1:
	st.markdown("<div class='section-header'>Economics Writing Guides</div>", unsafe_allow_html=True)
st.markdown("""
        1. **"Writing Economics" (Harvard University)**
           - Comprehensive guide for undergraduate economics writing
           - Available online through Harvard University

        2. **"The Economics of Economics Writing" (David Laibson, Harvard)**
           - Advanced guide focusing on professional economics writing
           - Emphasizes efficiency and clarity

        3. **"Writing Papers in Economics" (Jonathan Gruber, MIT)**
           - Focused on empirical economics papers
           - Strong emphasis on structure and argumentation

        4. **"A Guide for the Young Economist" (William Thomson)**
           - Book covering all aspects of economics research and writing
           - Particularly helpful for early-career economists

        5. **"The Economist's Craft" (Michael S. Weisbach)**
           - Recent book (2021) covering the entire research process
           - Includes modern perspectives on data and code
        """)

with col2:
	st.markdown("<div class='section-header'>Online Resources</div>", unsafe_allow_html=True)
st.markdown("""
        1. **Economics Journal Guidelines**
           - American Economic Association: https://www.aeaweb.org/journals/policies/submissions
           - Econometrica: https://www.econometricsociety.org/publications/econometrica/information-authors

        2. **Data and Code Repositories**
           - AEA Data and Code Repository: https://www.openicpsr.org/openicpsr/aea
           - Harvard Dataverse: https://dataverse.harvard.edu

        3. **Research Transparency**
           - Social Science Reproduction Platform: https://www.socialsciencereproduction.org
           - AEA RCT Registry: https://www.socialscienceregistry.org

        4. **LaTeX Resources**
           - Overleaf Economics Templates: https://www.overleaf.com/latex/templates/tagged/economics
           - LaTeXTemplates.com: Economics section

        5. **Economics Conferences Submission Guidelines**
           - NBER Summer Institute Guidelines
           - AEA/ASSA Annual Meeting Submission Guidelines
        """)

st.markdown(
	"<div class='highlight'>Effective economics writing combines technical precision with clear communication. The templates and resources provided here offer starting points, but remember to adapt them to your specific research question, methodology, and target journal. The most successful papers not only follow disciplinary conventions but also tell a compelling research story.</div>",
	unsafe_allow_html=True)

# Main page footer with attribution
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    Comprehensive Guide to Academic Writing in Economics<br>
    Developed by Dr. Merwan Roudane<br>
    © 2025 All Rights Reserved
</div>
""", unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
	st.sidebar.markdown("---")
st.sidebar.info("Contact: merwan.roudane@example.edu")