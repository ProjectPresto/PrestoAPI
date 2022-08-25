from django.template.defaultfilters import slugify


def createUniqueSlug(model, validated_data):
    if 'slug' not in validated_data:
        i = 0
        while True:
            newSlug = slugify(
                validated_data['name'] or validated_data['title']) if i == 0 else f"{(validated_data['name'] or validated_data['title'])}-{i}"
            if not model.objects.filter(slug=newSlug).exists():
                validated_data['slug'] = newSlug
                break
            i += 1
    return validated_data


def updateUniqueSlug(model, validated_data):
    if 'slug' not in validated_data:
        i = 0
        while True:
            newSlug = slugify(
                validated_data['name'] or validated_data['title']) if i == 0 else f"{newSlug}-{i}"
            if not model.objects.filter(slug=newSlug).exists():
                validated_data['slug'] = newSlug
                break
            i += 1
    return validated_data
