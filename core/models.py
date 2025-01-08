from django.db import models
import re

# For About Section
class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    email = models.EmailField()

    def __str__(self):
        return self.name


# For Projects Section
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True, null=True)  # General project URL (e.g., live site or GitHub)
    youtube_url = models.URLField(
        blank=True, 
        null=True,
        help_text="Add a YouTube URL if there's a demo video."
    )  # YouTube video URL for demo or overview
    technologies = models.CharField(
        max_length=200,
        help_text="Comma-separated list of technologies (e.g., Django, React, PostgreSQL)"
    )

    def get_youtube_video_id(self):
        # Extract YouTube video ID from the URL
        if self.youtube_url:
            match = re.search(r'(?<=v=)[\w-]+', self.youtube_url)
            if match:
                return match.group(0)
        return None

    def __str__(self):
        return self.title



# For Contact Section
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


# For Testimonials Section (Optional)
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    company = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='testimo/', blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}'s Testimonial"

