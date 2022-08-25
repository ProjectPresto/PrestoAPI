from django.template.defaultfilters import slugify


def createUniqueSlug(model, validated_data):
    if 'slug' not in validated_data:
        i = 0
        identifier = validated_data['name'] if 'name' in validated_data else validated_data['title']
        while True:
            newSlug = slugify(identifier) if i == 0 else f"{identifier}-{i}"
            if not model.objects.filter(slug=newSlug).exists():
                validated_data['slug'] = newSlug
                break
            i += 1
    return validated_data


def updateUniqueSlug(model, validated_data):
    if 'slug' not in validated_data:
        i = 0
        identifier = validated_data['name'] if 'name' in validated_data else validated_data['title']

        while True:
            newSlug = slugify(
                identifier) if i == 0 else f"{slugify(identifier)}-{i}"
            if not model.objects.filter(slug=newSlug).exists():
                validated_data['slug'] = newSlug
                break
            i += 1
    return validated_data
