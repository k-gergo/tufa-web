from django import template
import markdown
import re

register = template.Library()

@register.filter
def markdown_format(text):
    """Markdown formázást HTML-lé alakít."""
    if text:
        return markdown.markdown(text, extensions=['extra'])
    return ''

@register.filter
def embed_videos(content):
    """Átalakítja a YouTube és Vimeo URL-eket beágyazott videókká."""
    if not content:
        return ''
        
    # YouTube linkek átalakítása
    youtube_pattern = r'(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    youtube_replacement = r'<div class="video-container"><iframe width="100%" height="480" src="https://www.youtube.com/embed/\4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
    content = re.sub(youtube_pattern, youtube_replacement, content)
    
    # Vimeo linkek átalakítása
    vimeo_pattern = r'(https?:\/\/)?(www\.)?(vimeo\.com\/)(\d+)'
    vimeo_replacement = r'<div class="video-container"><iframe src="https://player.vimeo.com/video/\4" width="100%" height="480" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>'
    content = re.sub(vimeo_pattern, vimeo_replacement, content)
    
    return content