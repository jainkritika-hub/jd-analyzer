from pydantic import BaseModel, Field


class JobPosting(BaseModel):
    """Structured details extracted from a job description"""

    job_title: str = Field(description="The job title")
    company: str | None = Field(default=None, description="Company name, if mentioned")
    location: str | None = Field(default=None, description="Job location, if mentioned")
    employment_type: str | None = Field(
        default=None,
        description="Full-time, part-time, contract or internship, if mentioned",
    )
    min_experience_years: int | None = Field(
        default=None, description="Minimum years of experience required, if mentioned"
    )
    required_skills: list[str] = Field(
        description="Skills and tools the job requires"
    )
    nice_to_have_skills: list[str] = Field(
        default_factory=list,
        description="Skills listed as preferred or a plus",
    )
    responsibilities: list[str] = Field(
        description="Main duties of the role, as short phrases"
    )
    summary: str = Field(description="One-sentence summary of the role")