from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    has_reviewed = False
    user_review = None

    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            created_by=request.user,
            product=product
        ).first()

        has_reviewed = user_review is not None

    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content')

        if content:

            if has_reviewed:
                user_review.rating = rating
                user_review.content = content
                user_review.save()
            else:
                Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect('product', slug=slug)

    return render(request, 'product/product.html', {
        'product': product,
        'has_reviewed': has_reviewed,
        'user_review': user_review,
    })

@login_required
def remove_review(request, slug):
    product = get_object_or_404(Product, slug=slug)

    review = Review.objects.filter(product=product, created_by=request.user).first()
    if review:
        review.delete()

    return redirect('product', slug=slug)

@login_required
def edit_review(request, slug):
    product = get_object_or_404(Product, slug=slug)
    review = get_object_or_404(Review, product=product, created_by=request.user)

    if request.method == 'POST':
        rating = request.POST.get('rating', review.rating)
        content = request.POST.get('content', review.content)

        review.rating = rating
        review.content = content
        review.save()

        return redirect('product', slug=slug)  # back to product page

    return render(request, 'product/edit_review.html', {
        'product': product,
        'review': review
    })
