yayapf
========================================

yet another yapf. (the goal is removing this package)

supporting below format.

.. code-block:: python

  from foo import (
      x,
      y,
  )
  from foo import (  # NOQA
      x,
      y,
  )


sample .style.yapf

.. code-block::

  [style]
  based_on_style = pep8
  dedent_closing_brackets=true
