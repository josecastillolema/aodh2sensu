# How to contribute

## Testing

`pytest` and `flake8` are used for quality control.

To run all tests:

```bash
pytest
```

To run linting:

```bash
flake8 .
```

These steps are mandatory during the CI.

## Submitting changes

Please send a [GitHub Pull Request to opengovernment](https://github.com/opengovernment/opengovernment/pull/new/master) with a clear list of what you've done (read more about [pull requests](http://help.github.com/pull-requests/)). When you send a pull request, we will love you forever if you include RSpec examples. We can always use more test coverage. Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."
    
### Preparing your Fork

1. Click 'Fork' on Github, creating e.g. ``yourname/theproject``.
2. Clone your project: ``git clone git@github.com:yourname/theproject``.
3. ``cd theproject``
4. `Create and activate a virtual environment <https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments>`_.
5. Install the development requirements: ``pip install -r dev-requirements.txt``.
6. Create a branch: ``git checkout -b foo-the-bars 1.3``.

### Making your Changes

1. Add changelog entry crediting yourself.
2. Write tests expecting the correct/fixed functionality; make sure they fail.
3. Hack, hack, hack.
4. Run tests again, making sure they pass.
5. Commit your changes: ``git commit -m "Foo the bars"``

### Creating Pull Requests

1. Push your commit to get it back up to your fork: ``git push origin HEAD``
2. Visit Github, click handy "Pull request" button that it will make upon
   noticing your new branch.
3. In the description field, write down issue number (if submitting code fixing
   an existing issue) or describe the issue + your fix (if submitting a wholly
   new bugfix).
4. Hit 'submit'! And please be patient - the maintainers will get to you when
   they can.

## Coding conventions

  * **Follow the style you see used in the primary repository**! Consistency with
  the rest of the project always trumps other considerations. It doesn't matter
  if you have your own style or if the rest of the code breaks with the greater
  community - just follow along.
  * Python projects usually follow the `PEP-8
  <http://www.python.org/dev/peps/pep-0008/>`_ guidelines
  * We indent using two spaces (soft tabs)
  * We use HAML for all views
  * We avoid logic in views, putting HTML generators into helpers
  * We ALWAYS put spaces after list items and method parameters (`[1, 2, 3]`, not `[1,2,3]`), around operators (`x += 1`, not `x+=1`), and around hash arrows.
  * This is open source software. Consider the people who will read your code, and make it look nice for them. It's sort of like driving a car: Perhaps you love doing donuts when you're alone, but with passengers the goal is to make the ride as smooth as possible.
  * So that we can consistently serve images from the CDN, always use image_path or image_tag when referring to images. Never prepend "/images/" when using image_path or image_tag.
  * Also for the CDN, always use cwd-relative paths rather than root-relative paths in image URLs in any CSS. So instead of url('/images/blah.gif'), use url('../images/blah.gif').
