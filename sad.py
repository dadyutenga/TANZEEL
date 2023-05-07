# Create a new contribution
contribution = Contribution.objects.create(
    user=request.user,
    title='My Contribution',
    description='This is my contribution.',
    amount=100.00,
    date=date.today()
)

# Retrieve all contributions for a user
contributions = Contribution.objects.filter(user=request.user)

# Update a contribution
contribution.title = 'My Updated Contribution'
contribution.save()

# Delete a contribution
contribution.delete()
